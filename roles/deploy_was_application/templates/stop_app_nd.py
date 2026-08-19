
global AdminControl
global AdminConfig
global AdminClusterManagement

def check_if_cluster_exists(cluster_name):
  """Check if cluster exists"""
  cluster_exists = AdminClusterManagement.checkIfClusterExists(cluster_name)
  if not cluster_exists:
    raise Exception("check_if_cluster_exists: Unable to find Cluster '%s'" % (cluster_name))
  else:
    print ("check_if_cluster_exists: Cluster '%s' exists" % (cluster_name))

def check_application_status(app_name, server_name, node_name):
  """Check application status"""
  is_running = False
  # If the application is running, then an MBean is created. Otherwise, the command returns nothing
  app = AdminControl.completeObjectName('type=Application,name=%s,process=%s,node=%s,*' % (app_name,server_name,node_name))
  print ("check_application_status: Application '%s', MBean=%s" % ( app_name,repr(app) ))
  if len(app) == 0:
    is_running = False
    print ("check_application_status: Application %s is NOT RUNNING / NOT PRESENT on server %s, node %s" % (app_name,server_name,node_name))
  else:
    is_running = True
    print ("check_application_status: Application %s is RUNNING on server %s, node %s" % (app_name,server_name,node_name))
  return is_running

def stop_app(app_name, cluster_name):
  """Stop the named application"""

  print("stop_app: app_name=%s,cluster_name=%s" % (app_name,cluster_name))

  cell_name= AdminControl.getCell()

  # Sanity checks
  check_if_cluster_exists(cluster_name)

  # Get cluster members
  server_list = AdminClusterManagement.listClusterMembers(cluster_name)
  print ("stop_app: Cluster members %s" % ( repr(server_list) ))
  for server in server_list:
    server_name=AdminConfig.showAttribute(server, "memberName")
    node_name=AdminConfig.showAttribute(server, "nodeName")
    print ("stop_app: Stopping application - Node %s, Member %s" % (node_name, server_name))

    is_running = check_application_status(app_name, server_name, node_name)

    if is_running: # stop app
      # Get ApplicationManager
      app_manager = AdminControl.queryNames('cell=%s,node=%s,type=ApplicationManager,process=%s,*' % (cell_name,node_name,server_name))
      print ("stop_app: ApplicationManager - %s" % ( repr(app_manager) ))

      result_output = AdminControl.invoke(app_manager, 'stopApplication', app_name)
      print ("stop_app: stopApplication output - result_output=%s" % ( repr(result_output) ))
      print ("stop_app: Application %s STOPPED on server %s, node %s" % (app_name,server_name,node_name))

    else: # do nothing - app is not running / present
      print ("stop_app: Nothing to do for Application %s on server %s, node %s" % (app_name,server_name,node_name))


def main():

  stop_app(app_name='{{ env_vars.app_name }}', cluster_name='{{ env_vars.cluster_name }}')

if __name__ == "__main__":
  main()

