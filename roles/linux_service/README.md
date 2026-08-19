# linux_service

Configure Linux systemd services for managing WebSphere Application Server processes. This role creates, enables, and manages systemd unit files for WebSphere profiles and servers, allowing for standardized service control (start/stop/restart/status).

## Requirements

- Linux system with systemd (RHEL/CentOS/EL 8+)
- Sufficient privileges to create and manage systemd unit files
- WebSphere Application Server must be installed
- Profile and server names must be defined

## Role Variables

### Required Variables
| Variable         | Description                                 | Example                      |
|------------------|---------------------------------------------|------------------------------|
| `app`            | Service to create: standalone app, dmgr or ihs | `amtreports`              |
| `env_code`       | Environment code                           | `FATW`                        |

### Optional Variables
| Variable           | Default | Description                                  |
|--------------------|---------|----------------------------------------------|
| `dmgr_profile`     | `Dmgr01`   | Deployment Manager profile name           |
| `dmgr_server`      | `dmgr`     | Deployment Manager group name             |
| `nodeagent_profile`| `Custom01` | Node agent profile name                   |
| `nodeagent_server` | `nodeagent`| Node agent group name                     |

## Dependencies

None

## Tasks Performed

1. **Create Service**: Generates systemd unit file for WebSphere server
2. **Enable Service**: Enables the service to start at boot
3. **Allow webadmn and other users to sudo**: Add required users to sudoers for service management

## Notes

- Role is idempotent: safe to run multiple times
- Supports multiple profiles and servers
- Customizable user/group and service options
- Ensures standardized service management for WebSphere

## IBM Documentation

- [Managing WebSphere processes with systemd](https://www.ibm.com/docs/en/was-nd/9.0.5?topic=server-managing-processes-linux)
- [systemd unit files](https://www.freedesktop.org/software/systemd/man/systemd.unit.html)

## License

N/A
