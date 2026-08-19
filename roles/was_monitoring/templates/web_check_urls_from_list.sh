#!/bin/sh
URL_LIST_FILE="/opt/eteam/monitor_urls.list"
if [ ! -e $URL_LIST_FILE ]
then
    echo "No URLs to check"
    exit 0
fi

## Set exit codes up front
url_exit_code=0;
cert_exit_code=0;

## Loop URLs from file
while IFS="" read -r url || [ -n "$url" ]
do
  if [[ -n $url &&  ${url:0:1} != "#" ]] ; then  #if the line starts with # treat it as a comment

    ## explode URL to get protocol, uri and port - if port is not set use default for HTTPS vs HTTP
    PROTOCOL=`echo $url | cut -d ":" -f 1`
    URI=`echo $url | cut -d / -f 3`
    PORT="$(echo $url | sed -e 's,^.*:,:,g' -e 's,.*:\([0-9]*\).*,\1,g' -e 's,[^0-9],,g')"
    if [[ $PORT == "" ]];
    then
      if [[ $PROTOCOL == "https" ]];
      then
              PORT="443"
      else
              PORT="80"
      fi
    fi

    ## Get response code for URL - Accept 301. 302 and 200. If the URL is available move onto SSL check
    OUTPUT=`curl -k -s -m 30 -o /dev/null --write-out '%{http_code}\n' $url`
    if [[ $OUTPUT != 301 && $OUTPUT != "302" && $OUTPUT != "200" ]];
    then
            url_exit_code=2 #end with critical
            echo "$url is unavailable"
    else

            ## If URL is SSL then check certificate, if certs +27 days okay, 14 - 27 WARN, 14 Critical
            if [[ $PROTOCOL == "https" ]];
            then
                get_cert_date=`echo | openssl s_client -connect $URI:$PORT 2>/dev/null | openssl x509 -enddate -noout`
                if [[ $? -eq 0 ]]; then
                  extract_date=`echo $get_cert_date | cut -d= -f 2`
                  remaining=$(( ($(date -d "$extract_date" +%s) - $(date +%s))/84600))
                  if [[ $remaining -gt 27 ]]; then
                    exit_code=0 #Okay
                  elif [[ $remaining -lt 28 && $remaining -gt 14 ]]; then
                    exit_code=1 #Warning
                    echo "$url expires in "$remaining" days"
                  else
                    exit_code=2 #Critical
                    echo "$url expires in "$remaining" days"
                  fi
                  if [[ $exit_code > $cert_exit_code ]];then
                          cert_exit_code=$exit_code
                  fi
                fi
        fi

    fi
  fi
done <$URL_LIST_FILE

## Exit with the highest return code 0 = Okay, 1 = Warning, 2 = Critical, 3+ = Unknown
if [[ $cert_exit_code > $url_exit_code ]];
then
  if [[ $cert_exit_code == 0 ]]; then echo "All checks were successful";fi
  exit $cert_exit_code
else
  if [[ $url_exit_code == 0 ]]; then echo "All checks were successful";fi
  exit $url_exit_code
fi
