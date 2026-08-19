# start_service

Start WebSphere Application Server standalone services using systemctl.

## Requirements

- WebSphere standalone profile must be configured
- Application must be deployed
- Linux service must be configured for WebSphere
- systemctl must be available

## Role Variables

### Required Variables
| Variable | Description | Example |
|----------|-------------|---------|
| `app` | Application name | `amtreports` |

### Default Variables
| Variable | Default | Description |
|----------|---------|-------------|

## Dependencies

- `linux_service`: Service must be configured before starting

## Tasks Performed

1. **Validation**: Ensures application is standalone (not clustered)
2. **Variable Setup**: Sets service name based on application configuration
3. **Service Start**: Uses systemctl to start the WebSphere service
4. **Status Check**: Verifies service started successfully

## Notes

- Only works with standalone WebSphere installations
- Will fail if application is part of a Network Deployment cluster
- Uses systemctl to manage services
- Service name is derived from application and profile names
- Idempotent - safe to run multiple times

## Error Handling

- Validates that `env_vars.dmgr_host` is not defined (ensures standalone)
- Checks service status before and after start operation
- Provides clear error messages for troubleshooting

## IBM Documentation

- [Starting and stopping servers](https://www.ibm.com/docs/en/was-nd/9.0.5?topic=administration-starting-stopping-servers)
- [Server startup troubleshooting](https://www.ibm.com/docs/en/was-nd/9.0.5?topic=servers-troubleshooting-server-startup)

## License

N/A
