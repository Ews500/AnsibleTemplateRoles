
global AdminApp
global AdminConfig
global AdminControl
global AdminServerManagement

def check_if_server_exists(server_name,node_name):
  """Check if server exists"""
  server_exists = AdminServerManagement.checkIfServerExists(node_name, server_name)
  if not server_exists:
    raise Exception("check_if_server_exists: Unable to find Server '%s' on node %s" % (server_name,node_name))
  else:
    print ("check_if_server_exists: Server '%s' exists on node %s" % (server_name,node_name))

def uninstall_app(app_name, server_name):
  """Uninstall the named application"""

  print("uninstall_app: app_name=%s,server_name=%s" %(app_name,server_name))

  node_name = AdminControl.getNode()

  # Sanity checks
  check_if_server_exists(server_name,node_name)

  # Uninstall application
  # If the app is not installed an exception is raised when calling AdminApp.uninstall
  # WASX7280E: An application with name "XXXX" does not exist.
  try:
    AdminApp.uninstall(app_name)
    AdminConfig.save()
  except:
    print ("uninstall_app: Application %s DOES NOT EXISTS (not installed)" % (app_name))


def main():
  uninstall_app(app_name='{{ env_vars.app_name }}', server_name='{{ env_vars.server_name }}')

if __name__ == "__main__":
  main()

