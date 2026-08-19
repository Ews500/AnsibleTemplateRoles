import time

global AdminControl
global AdminConfig
global AdminApp
global AdminServerManagement

def check_if_server_exists(server_name,node_name):
  """Check if server exists"""
  server_exists = AdminServerManagement.checkIfServerExists(node_name, server_name)
  if not server_exists:
    raise Exception("check_if_server_exists: Unable to find Server '%s' on node %s" % (server_name,node_name))
  else:
    print ("check_if_server_exists: Server '%s' exists on node %s" % (server_name,node_name))

def start_app(app_name, server_name):
  """Start the named application"""

  print("start_app: app_name=%s,server_name=%s" %(app_name,server_name))

  cell_name= AdminControl.getCell()
  node_name = AdminControl.getNode()
  print ("start_app: Starting application - Node %s, Server %s" % (node_name, server_name))

  # Sanity checks
  check_if_server_exists(server_name,node_name)

  # Get ApplicationManager
  app_manager = AdminControl.queryNames('cell=%s,node=%s,type=ApplicationManager,process=%s,*' %(cell_name,node_name,server_name))
  print ("start_app: ApplicationManager - %s" % ( repr(app_manager) ))

  # start app
  result_output = AdminControl.invoke(app_manager, 'startApplication', app_name)
  print ("start_app: startApplication output - result_output=%s" % ( repr(result_output) ))
  print ("start_app: Application %s STARTED on server %s, node %s" % (app_name,server_name,node_name))


def main():
  
  start_app(app_name='{{ env_vars.app_name }}', server_name='{{ env_vars.server_name }}')

if __name__ == "__main__":
  main()
