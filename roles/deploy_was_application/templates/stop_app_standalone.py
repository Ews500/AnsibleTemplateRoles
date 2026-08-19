import time

global AdminControl
global AdminConfig
global AdminServerManagement

def check_if_server_exists(server_name,node_name):
  """Check if server exists"""
  server_exists = AdminServerManagement.checkIfServerExists(node_name, server_name)
  if not server_exists:
    raise Exception("check_if_server_exists: Unable to find Server '%s' on node %s" % (server_name,node_name))
  else:
    print ("check_if_server_exists: Server '%s' exists on node %s" % (server_name,node_name))

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

def stop_app(app_name, server_name):
  """Stop the named application"""

  print("stop_app: app_name=%s,server_name=%s" %(app_name,server_name))

  cell_name= AdminControl.getCell()
  node_name = AdminControl.getNode()
  print ("stop_app: Stopping application - Node %s, Server %s" % (node_name, server_name))

  # Sanity checks
  check_if_server_exists(server_name,node_name)

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

  stop_app(app_name='{{ env_vars.app_name }}', server_name='{{ env_vars.server_name }}')

if __name__ == "__main__":
  main()

