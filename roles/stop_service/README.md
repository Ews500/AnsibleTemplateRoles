# stop_service

Stop WebSphere Application Server standalone services using systemctl.

## Requirements

- WebSphere standalone profile must be running
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

- `linux_service`: Service must be configured

## Tasks Performed

1. **Validation**: Ensures application is standalone (not clustered)
2. **Variable Setup**: Sets service name based on application configuration
3. **Service Stop**: Uses systemctl to stop the WebSphere service gracefully
4. **Status Check**: Verifies service stopped successfully

## Notes

- Only works with standalone WebSphere installations
- Will fail if application is part of a Network Deployment cluster
- Uses systemctl to manage services
- Graceful shutdown with timeout handling
- Idempotent - safe to run multiple times

## License

N/A
