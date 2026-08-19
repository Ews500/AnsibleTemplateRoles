
global AdminApp
global AdminConfig
global AdminControl
global AdminClusterManagement

def check_if_cluster_exists(cluster_name):
  """Check if cluster exists"""
  cluster_exists = AdminClusterManagement.checkIfClusterExists(cluster_name)
  if not cluster_exists:
    raise Exception("check_if_cluster_exists: Unable to find Cluster '%s'" % (cluster_name))
  else:
    print ("check_if_cluster_exists: Cluster '%s' exists" % (cluster_name))

def uninstall_app(app_name, cluster_name):
  """Uninstall the named application"""

  print("uninstall_app: app_name=%s,server_name=%s" %(app_name,cluster_name))

  # Sanity checks
  check_if_cluster_exists(cluster_name)

  # Uninstall application
  # If the app is not installed an exception is raised when calling AdminApp.uninstall
  # WASX7280E: An application with name "XXXX" does not exist.
  try:
    AdminApp.uninstall(app_name)
    AdminConfig.save()
  except:
    print ("uninstall_app: Application %s DOES NOT EXISTS (not installed)" % (app_name))

def main():
  uninstall_app(app_name='{{ env_vars.app_name }}', cluster_name='{{ env_vars.cluster_name }}')

if __name__ == "__main__":
  main()

