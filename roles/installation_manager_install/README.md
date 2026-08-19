# installation_manager_install

Install IBM Installation Manager, the prerequisite for installing IBM software products.

## Requirements

- Linux system prepared for IBM software
- Access to IBM Installation Manager installation media
- webadmn user must exist

## Role Variables

### Required Variables
| Variable | Description | Example |
|----------|-------------|---------|
| `iim_version` | Installation Manager version | `1.9.2002.20220323_1321` |
| `iim_bin_file` | Installation Manager binary file | `agent.installer.linux.gtk.x86_64_1.9.2002.20220323_1321.zip` |
| `iim_install_location` | Installation Manager installation directory | `/app/InstallationManager` |

### Default Variables
| Variable | Default | Description |
|----------|---------|-------------|
| `iim_data_location` | `/app/InstallationManagerData` | Installation Manager data location |
| `imshared_location` | `/app/IMShared` | Installation Manager shared location |
| `shared_mount` | `/nfstemp/was_binaries` | Binaries location |

## Dependencies

- `ibm_linux`: Ensures system is prepared for IBM software

## Example Playbook

```yaml
---
- hosts: websphere_servers
  roles:
    - role: installation_manager_install
      vars:
        iim_version: "1.9.2002.20220323_1321"
        iim_data_location: "agent.installer.linux.gtk.x86_64_1.9.2002.20220323_1321.zip"
```

## Tags

- `iim_install`: Run complete Installation Manager installation

## Tasks Performed

1. **Version Check**: Verifies if Installation Manager is already installed
2. **Installation**: Installs IBM Installation Manager if not present
3. **Configuration**: Sets up Installation Manager for subsequent IBM software installations

## Notes

- Installation Manager is a prerequisite for all IBM software installations
- Role is idempotent - checks for existing installation before proceeding
- Runs as webadmn user for proper permissions
- Required for WebSphere, HTTP Server, and other IBM products

## IBM Documentation

- [Installing IBM Installation Manager](https://www.ibm.com/docs/en/installation-manager/1.9.2?topic=installing-installation-manager)
- [Installation Manager overview](https://www.ibm.com/docs/en/installation-manager/1.9.2?topic=overview)

## License

N/A
