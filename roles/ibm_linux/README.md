# ibm_linux

Prepare Linux systems for IBM software installation including user creation, package installation, and system configuration.

## Requirements

- Red Hat Enterprise Linux or compatible distribution
- Root access on target systems
- Network access to package repositories

## Role Variables

### Required Variables
| Variable | Description | Example |
|----------|-------------|---------|
| `webadmn_user` | WebSphere admin user | `webadmn` |
| `webadmn_group` | WebSphere admin group | `webadmn` |

### Default Variables
| Variable | Default | Description |
|----------|---------|-------------|
| `nfs_volume` | `bc21:/software/Oracle_Software/was` | NFS volume for IBM software |
| `nfs_mountpoint` | `/nfstemp` | NFS mount point for IBM software |
| `atradius_webteam_accounts` | Dict with users | Atradius Web Team members |
| `infosys_webteam_accounts` | Dict with users | Infosys Web Team members |
| `operations_team_accounts` | Dict with users | Operations Team members |
| `removed_webteam_accounts` | Dict with users | Removed Web Team members |

## Dependencies

None

## Example Playbook

```yaml
---
- name: Setting up linux host
  hosts: all
  become: true
  become_user: root
  gather_subset:
    - '!all'
    - 'min'
  roles:
    - ibm_linux
```

## Tags

- `webadmn_setup`: Create webadmn user and group only
- `devops_ssh`: Configure SSH access for DevOps user
- `create_dirs`: Create necessary directories
- `rpm_install`: Install RPM packages
- `create_users`: Create necessary user accounts
- `nfs_mount`: Configure NFS mounts
- `ulimits`: Configure ulimits

## Tasks Performed

1. **User Management**:
   - Creates `webadmn` group with GID 700
   - Creates `webadmn` user with UID 700
   - Sets up home directory and permissions

2. **Package Installation**:
   - Installs required packages for IBM software
   - Updates system packages as needed

3. **System Configuration**:
   - Configures system settings for optimal IBM software performance
   - Sets up environment variables
   - Configures kernel parameters if needed

## Host Variables

This role includes host-specific variables from:
`environments/{{ env_code }}/host_vars/{{ inventory_hostname_short }}.yml`

## Notes

- Run this role before installing any IBM software
- Limit the role to specific hosts or groups as needed
- Requires root privileges for user creation and system configuration
- Idempotent - safe to run multiple times

## License

N/A
