# http_server_install

Install IBM HTTP Server, Web Server Plug-ins and Web Server Customization Toolbox.

## Requirements

- IBM Installation Manager must be installed
- Target group must be 'ihs'
- IBM HTTP Server installation media must be accessible
- Java SDK must be available

## Role Variables

### Required Variables
| Variable | Description | Example |
|----------|-------------|---------|
| `target_group` | Must be 'ihs' for this role | `ihs` |


### Default Variables
| Variable | Default | Description |
|----------|---------|-------------|
| `ihs_vars.base_release` | `9.0.5.01` | IHS base release version |
| `ihsplg_vars.target_fixpack` | `9.0.5.23` | IHS target plug-in fixpack |
| `ihswct_vars.target_fixpack` | `9.0.5.23` | IHS WCT target fixpack |
| `java_vars.base_release` | `8.0.5.0` | JDK base version |
| `java_vars.target_fixpack` | `8.0.8.40` | JDK target fixpack level |
| `iim_install_location` | `/app/InstallationManager` | Installation Manager location |
| `iim_data_location` | `/app/InstallationManagerData` | Installation Manager data location |
| `imshared_location` | `/app/IMShared` | Installation Manager shared location |
| `shared_mount` | `/nfstemp/was_binaries` | Binaries location |


## Dependencies

- `installation_manager_install`: Ensures IBM Installation Manager is installed
- `ibm_linux`: Prepares Linux system for IBM software

## Example Playbook

```yaml
---
- name: Install IBM HTTP Web Server Plugin and WCT
  hosts: "{{ target_group | default('null') }}"
  become: true
  become_user: webadmn

  pre_tasks:
    - name: Fail if target_group is not 'ihs'
      ansible.builtin.fail:
        msg: "This playbook is intended to be run only for target_group='ihs' (web servers). Current value: {{ target_group }}"
      when: target_group != 'ihs'

  roles:
    - installation_manager_install  # shared across products
    - http_server_install           # handles ihs logic internally
```

## Tags

- `ihs_install`: Run complete IBM HTTP Server installation
- `install_ihs_standalone`: Run IBM HTTP Server standalone installation

## Components Installed

1. **IBM HTTP Server (IHS)**: Web server component
2. **Web Server Plug-ins**: Integration between IHS and WebSphere
3. **Web Server Customization Toolbox (WCT)**: Configuration tools

## Notes

- Installation requires significant disk space (2GB+)
- Process can take 20-40 minutes depending on system performance
- Role will fail if target_group is not 'ihs'
- Verify system requirements before running

## IBM Documentation

- [Installing IBM HTTP Server](https://www.ibm.com/docs/en/was-nd/9.0.5?topic=server-installing-ibm-http)
- [Installing the Web Server Plug-ins](https://www.ibm.com/docs/en/was-nd/9.0.5?topic=installing-web-server-plug-ins)

## License

N/A
