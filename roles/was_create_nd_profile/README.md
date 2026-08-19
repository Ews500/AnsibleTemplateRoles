# was_create_nd_profile

Create and configure a WebSphere Network Deployment (ND) profile. This role checks for the existence of the profile, creates it if missing, configures security, federates the node, and starts the node agent.

## Requirements

- WebSphere Application Server ND must be installed
- Sufficient privileges to create and configure profiles
- Required variables set for profile directory and configuration

## Role Variables

### Required Variables
| Variable | Description | Example |
|----------|-------------|---------|
| `app` | Profile name to create | `genericbip-ie` |
| `env_code` | Environment code | `FATW` |

### Optional Variables

Check roles/was_create_nd_profile/vars/main.yml file for default values.

## Dependencies

- `was_install`: WebSphere ND must be installed first

## Tags

- `check_profile`: Check if the profile exists
- `create_profile`: Create the ND profile if missing
- `config_profile`: Configure the profile
- `set_security`: Set profile security
- `federate_node`: Federate the node to the cell
- `start_nodeagent`: Start the node agent

## Tasks Performed

1. **Check Profile**: Verifies if the ND profile directory exists
2. **Create Profile**: Creates the ND profile if it does not exist
3. **Configure Profile**: Sets security, federates node, and starts node agent (if enabled)

## Notes

- Role is idempotent: safe to run multiple times
- Uses blocks and conditional logic for safe operations
- Ensure all required variables are set for your environment

## IBM Documentation

- [Creating Network Deployment profiles](https://www.ibm.com/docs/en/was-nd/9.0.5?topic=line-creating-profiles-manageprofiles-command)
- [Federating nodes](https://www.ibm.com/docs/en/was-nd/9.0.5?topic=nodes-federating)
- [Node agent management](https://www.ibm.com/docs/en/was-nd/9.0.5?topic=agents-node-agent-management)

## License

N/A
