# was_install

Install IBM WebSphere Application Server using IBM Installation Manager.

## Requirements

- IBM Installation Manager must be available
- WebSphere installation media must be accessible
- Target system must meet WebSphere requirements

## Role Variables

### Required Variables
| Variable | Description | Example |
|----------|-------------|---------|
| `target_group` | Type of installation (standalone/nd/dmgr) | `standalone` |
| `env_code` | Environment code | `FATW` |

### Default Variables
| Variable | Default | Description |
|----------|---------|-------------|
| `was_vars.base_release` | `9.0.5.01` | WebSphere base version |
| `was_vars.target_fixpack` | `9.0.5.23` | WebSphere target fixpack level |
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
- name: Install and patch WebSphere Application Server
  hosts: "{{ target_group | default('null') }}"
  become: true
  become_user: webadmn
  roles:
    - installation_manager_install
    - was_install
```

## Tags

- `was_install`: Run complete WebSphere installation
- `install_was_standalone`: Run standalone WebSphere installation
- `install_nd`: Run Network Deployment installation
- `install_dmgr`: Run Deployment Manager installation

## Notes

- Installation requires significant disk space (4GB+)
- Process can take 30-60 minutes depending on system performance
- Verify system requirements before running