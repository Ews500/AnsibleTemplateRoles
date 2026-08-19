
global AdminControl

def start_job(mbean_name):
  """Start the named mbean job"""

  print("start_job: mbean_name=%s" % (mbean_name))

  # get a MBean-object for the job of ineterst
  job = AdminControl.queryNames ("*:*,name=%s" % (mbean_name))
  print("start_job: job=%s" % (repr(job)))

  # this is the point where we actually start the MBean. This call will take long
  job_result = AdminControl.invoke(job, "start")
  print("start_job: job_result=%s" % (repr(job_result)))

  # return the return-value to shell level
  java.lang.System.exit( int(job_result))

def main():
  start_job(mbean_name='{{ mbean_name }}')

if __name__ == "__main__":
  main()

