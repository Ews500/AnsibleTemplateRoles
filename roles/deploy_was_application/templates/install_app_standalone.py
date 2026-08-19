import time

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


def modify_app_classloader(app_name):
  """Modify Application Classloader settings to 'PARENT_LAST'"""
  # https://www.ibm.com/docs/en/was-nd/9.0.5?topic=caus-modifying-class-loader-modes-applications-using-wsadmin-scripting

  print ("modify_app_classloader: Modifying Application Classloader settings to 'PARENT_LAST'")
  deployment = AdminConfig.getid('/Deployment:'+app_name+'/')
  deployment_object = AdminConfig.showAttribute(deployment, 'deployedObject')
  classldr = AdminConfig.showAttribute(deployment_object, 'classloader')
  AdminConfig.modify(classldr, [['mode', 'PARENT_LAST']])
  AdminConfig.save()
  print("modify_app_classloader: showall=%s" % ( repr(AdminConfig.showall(classldr))))

def modify_war_classloader(app_name):
  """Modify WAR Modules Classloader settings to 'PARENT_LAST'"""
  # https://www.ibm.com/docs/en/was-nd/9.0.5?topic=caus-modifying-war-class-loader-mode-using-wsadmin-scripting

  print ("modify_war_classloader: Modifying WAR Modules Classloader settings to 'PARENT_LAST'")
  deployment = AdminConfig.getid('/Deployment:'+app_name+'/')
  deployment_object = AdminConfig.showAttribute(deployment, 'deployedObject')
  modules_list = AdminConfig.showAttribute(deployment_object, 'modules')
  modules_list = modules_list[1:len(modules_list)-1].split(" ")
  print("modify_war_classloader: modules_list=%s" % ( repr(modules_list)))
  for module in modules_list:
   if (module.find('WebModuleDeployment')!= -1):
    AdminConfig.modify(module, [['classloaderMode', 'PARENT_LAST']])
  AdminConfig.save()
  print("modify_war_classloader: showall=%s" % ( repr(AdminConfig.showall(module))))

def modify_war_classloader_policy(app_name):
  """Modifying WAR class loader policies"""
  # https://www.ibm.com/docs/en/was/9.0.5?topic=caus-modifying-war-class-loader-policies-applications-using-wsadmin-scripting
  # warClassLoaderPolicy - Default value is MULTIPLE. Other possible value is SINGLE

  print ("modify_war_classloader_policy: Modifying WAR class loader policies")
  deployment = AdminConfig.getid('/Deployment:'+app_name+'/')
  deployment_object = AdminConfig.showAttribute(deployment, 'deployedObject')
  print("modify_war_classloader_policy: Default warClassLoaderPolicy=%s" % ( repr(AdminConfig.show(deployment_object, 'warClassLoaderPolicy'))))
  AdminConfig.modify(deployment_object, [['warClassLoaderPolicy', '{{ app_vars.war_classloader_policy|default(app_defaults.war_classloader_policy) }}']])
  AdminConfig.save()
  print("modify_war_classloader_policy: Updated warClassLoaderPolicy=%s" % ( repr(AdminConfig.show(deployment_object, 'warClassLoaderPolicy'))))

def install_app(file_name, app_name, server_name):
  """Install the named application"""

  print("install_app: file_name=%s,app_name=%s,server_name=%s" %(file_name,app_name,server_name))

  node_name = AdminControl.getNode()

  # Sanity checks
  check_if_server_exists(server_name,node_name)

  #####
  app_settings = ["-appname", app_name, "-node", node_name, "-server", server_name]
  
  # Other options are loaded from environment variables file
{% for option in app_vars.app_options|default(app_defaults.app_options) %}
{% if option.type == "array" %} 
  app_settings.extend(["{{ option.name }}",[[ {{ option.value | map('to_json') | join(', ') }} ]]  ]) # Don't add double quotes
{% else %}
  app_settings.extend(["{{ option.name }}","{{ option.value }}"])
{% endif %}
{% endfor %}

  print("install_app: app_settings=%s" % ( repr(app_settings)))
  AdminApp.install(file_name,app_settings)
  AdminConfig.save()
  # Wait 30 seconds
  time.sleep(30)

  # Modify Application and WAR Modules Classloader settings to 'PARENT_LAST'. Only IF mod_classldr var is defined in the inventory
{% if app_vars.mod_classldr | default(app_defaults.mod_classldr) %}
  modify_app_classloader(app_name)
  modify_war_classloader(app_name)
{% endif %}
  modify_war_classloader_policy(app_name)

def main():
  install_app(file_name='{{ env_vars.app_name }}.ear', app_name='{{ env_vars.app_name }}', server_name='{{ env_vars.server_name }}')

if __name__ == "__main__":
  main()

