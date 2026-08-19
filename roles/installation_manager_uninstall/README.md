# installation_manager_uninstall

Completely remove IBM Installation Manager and all associated directories from the system.

## Requirements

- IBM Installation Manager must be installed on the target system
- Sufficient privileges to remove directories
- All IBM products installed via Installation Manager should be uninstalled first

## Role Variables

### Default Variables
| Variable | Default | Description |
|----------|---------|-------------|
| `iim_install_location` | `/app/InstallationManager` | Installation Manager binary directory |
| `iim_data_location` | `/app/InstallationManagerData` | Installation Manager data directory |
| `imshared_location` | `/app/IMShared` | Installation Manager shared resources directory |

### Variable Override
You can override these variables if your Installation Manager is installed in different locations:

```yaml
vars:
  iim_install_location: "/opt/IBM/InstallationManager"
  iim_data_location: "/var/ibm/InstallationManager"
  imshared_location: "/opt/IBM/IMShared"
```

## Dependencies

None

## Example Playbook

```yaml
---
- hosts: websphere_servers
  roles:
    - role: installation_manager_uninstall
```

## Example with Custom Locations

```yaml
---
- hosts: websphere_servers
  roles:
    - role: installation_manager_uninstall
      vars:
        iim_install_location: "/opt/IBM/InstallationManager"
        iim_data_location: "/var/ibm/InstallationManager"
        imshared_location: "/opt/IBM/IMShared"
```

## Tasks Performed

This role performs a complete cleanup of IBM Installation Manager by:

1. **Remove Installation Directory**: Recursively removes the Installation Manager binary directory
2. **Remove Data Directory**: Recursively removes the Installation Manager data directory  
3. **Remove Shared Directory**: Recursively removes the Installation Manager shared resources directory

## ⚠️ Important Notes

- **Destructive Operation**: This role permanently removes all Installation Manager directories and data
- **Prerequisites**: Ensure all IBM products (WebSphere, HTTP Server, etc.) are uninstalled before running this role
- **No Rollback**: Once executed, Installation Manager must be reinstalled from scratch if needed
- **Idempotent**: Safe to run multiple times - will not fail if directories don't exist
- **File Permissions**: Ensure the user has sufficient privileges to remove the specified directories

## Use Cases

- **Environment Cleanup**: Complete removal of IBM software stack
- **Fresh Installation**: Preparing system for clean Installation Manager reinstall
- **Decommissioning**: Removing IBM software from retired systems
- **Troubleshooting**: Resolving Installation Manager corruption issues

## IBM Documentation

- [Uninstalling IBM Installation Manager](https://www.ibm.com/docs/en/installation-manager/1.9.2?topic=uninstalling-installation-manager)
- [Installation Manager directory structure](https://www.ibm.com/docs/en/installation-manager/1.9.2?topic=reference-installation-manager-directory-structure)

## License

N/A
