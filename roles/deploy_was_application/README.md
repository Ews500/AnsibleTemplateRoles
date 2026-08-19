# deploy_was_application

The `deploy_was_application` role will deploy an application in WebSphere Application Server.

## Requirements

- Define application name in `environments/<env_code>/hosts` files. This name will be later use as `app` variable in the role.
- Include vault file for that particular environment (`environments/<env_code>/vault.yml`) to ensure all variables are loaded.
- `app_vars` (`environments/app_vars/<app>.yml`) and `env_vars` (`environments/<env_code>/group_vars/<app>.yml`) files must exist for the `app` that will be deployed.

## Role Variables

| Variable       | Default | Required | Description                     |
|----------------|---------|----------|---------------------------------|
| `app`          | N/A     | Yes      | Application name to deploy      |


## Dependencies

None

## Example Playbook

```
- name: Deploy Websphere Application
  hosts: "{{ app | default('null') }}"
  tasks:
    - name: Deploy application
      ansible.builtin.include_role:
        name: deploy_was_application
```

## IBM Installation Manager Documentation
- [Scripting the application serving environment (wsadmin)](https://www.ibm.com/docs/en/was-nd/9.0.5?topic=90-scripting-application-serving-environment-wsadmin)
- [EARExpander command](https://www.ibm.com/docs/en/was/9.0.5?topic=tools-earexpander-command)
- [Stopping applications using wsadmin scripting](https://www.ibm.com/docs/en/was-nd/9.0.5?topic=scripting-stopping-applications-using-wsadmin)
- [Starting applications using wsadmin scripting](https://www.ibm.com/docs/en/was-nd/9.0.5?topic=scripting-starting-applications-using-wsadmin)
- [Stopping servers using scripting](https://www.ibm.com/docs/en/was/9.0.5?topic=scripting-stopping-servers-using)
- [Starting servers using scripting](https://www.ibm.com/docs/en/was/9.0.5?topic=scripting-starting-servers-using)
- [Uninstalling enterprise applications using the wsadmin scripting tool](https://www.ibm.com/docs/en/was-nd/9.0.5?topic=scripting-uninstalling-enterprise-applications-using-wsadmin-tool)
- [Installing enterprise applications using wsadmin scripting](https://www.ibm.com/docs/en/was-nd/9.0.5?topic=scripting-installing-enterprise-applications-using-wsadmin)
- [Modifying WAR class loader mode using wsadmin scripting](https://www.ibm.com/docs/en/was-nd/9.0.5?topic=caus-modifying-war-class-loader-mode-using-wsadmin-scripting)
- [Commands for the AdminControl object using wsadmin scripting](https://www.ibm.com/docs/en/was/9.0.5?topic=scripting-commands-admincontrol-object-using-wsadmin)
- [Commands for the AdminApp object using wsadmin scripting](https://www.ibm.com/docs/en/was/9.0.5?topic=scripting-commands-adminapp-object-using-wsadmin)

## License

N/A
