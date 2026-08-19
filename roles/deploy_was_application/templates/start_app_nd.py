import time

global AdminControl
global AdminConfig
global AdminApp
global AdminClusterManagement

def check_if_cluster_exists(cluster_name):
  """Check if cluster exists"""
  cluster_exists = AdminClusterManagement.checkIfClusterExists(cluster_name)
  if not cluster_exists:
    raise Exception("check_if_cluster_exists: Unable to find Cluster '%s'" % (cluster_name))
  else:
    print ("check_if_cluster_exists: Cluster '%s' exists" % (cluster_name))


def start_app(app_name, cluster_name):
  """Start the named application"""

  print("start_app: app_name=%s,cluster_name=%s" %(app_name,cluster_name))

  cell_name= AdminControl.getCell()

  # Sanity checks
  check_if_cluster_exists(cluster_name)

  server_list = AdminClusterManagement.listClusterMembers(cluster_name)
  print ("start_app: Cluster members %s" % ( repr(server_list) ))
  for server in server_list:
    server_name=AdminConfig.showAttribute(server, "memberName")
    node_name=AdminConfig.showAttribute(server, "nodeName")
    print ("start_app: Starting application - Node %s, Member %s" % (node_name, server_name))

    AdminApp.isAppReady(app_name)
    is_app_ready = AdminApp.isAppReady(app_name)
    print ("start_app: is_app_ready - %s" % ( repr(is_app_ready ) ))  

    # Get ApplicationManager
    app_manager = AdminControl.queryNames('cell=%s,node=%s,type=ApplicationManager,process=%s,*' %(cell_name,node_name,server_name))
    print ("start_app: ApplicationManager - %s" % ( repr(app_manager) ))
    
    # start app
    result_output = AdminControl.invoke(app_manager, 'startApplication', app_name)
    print ("start_app: startApplication output - result_output=%s" % ( repr(result_output) ))
    print ("start_app: Application %s STARTED on server %s, node %s" % (app_name,server_name,node_name))

def main():
  
  start_app(app_name='{{ env_vars.app_name }}', cluster_name='{{ env_vars.cluster_name }}')

if __name__ == "__main__":
  main()
