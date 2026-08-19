# create_sysman

Create /sysman/operators directories and scripts for WebSphere start and stop operations.

## Requirements

- Root access on target systems
- WebSphere application server must be installed

## Role Variables

### Required Variables
| Variable | Description | Example |
|----------|-------------|---------|

### Default Variables
| Variable | Default | Description |
|----------|---------|-------------|
| `sysman_dir` | `/sysman/operators` | System management scripts directory |
| `log_dir` | `/var/log/websphere` | WebSphere log directory |

## Dependencies

None

## Example Playbook

```yaml
---
- name: Create sysman scripts from ND hosts
  hosts: nd
  gather_subset:
    - '!all'
    - 'min'
    - 'network'
  roles:
    - create_sysman
```

## Tags

- `create_dirs`: Create required directories only
- `all_appservers`: Template start & stop script for all envs and applications
- `all_env_applications`: Template start & stop scripts for all envs

## Templates

- `start_websphere_all_appservers.j2`: Script to start all application servers in the box
- `stop_websphere_all_appservers.j2`: Script to stop all application servers in the box
- `start_websphere_all_env_applications.j2`: Script to start all application servers in a specific environment (FATW, FATF, BAT...) the box
- `stop_websphere_all_env_applications.j2`: Script to stop all application servers in a specific environment (FATW, FATF, BAT...) the box

## Notes

- Creates `/sysman/operators` directory for operational scripts
- Creates `/var/log/websphere` directory for WebSphere logs
- Scripts are owned by root with 755 permissions

## License

N/A
