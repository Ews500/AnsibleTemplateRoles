# was_create_ndapp_cluster_servers

Create and configure application servers within a WebSphere Network Deployment (ND) cluster. This role is typically used after the ND profile and cell have been created and federated.

## Requirements

- WebSphere Application Server ND must be installed
- ND profile and cell must already exist and be federated
- Sufficient privileges to create and configure cluster servers
- Required variables set for cluster and server configuration

## Role Variables

### Required Variables
| Variable         | Description                                 | Example                      |
|------------------|---------------------------------------------|------------------------------|
| `app` | Profile name to create | `genericbip-ie` |
| `env_code` | Environment code | `FATW` |

### Optional Variables

Check roles/was_create_ndapp_cluster_servers/vars/main.yml file for default values.

## Dependencies

- `was_create_nd_profile`: ND profile and cell must be created and federated first

## Tags

- `create_cluster_servers`: Create application servers in the ND cluster
- `config_cluster`: Configure cluster settings
- `config_nodeservers`: Configure node servers after creation

## Tasks Performed

1. **Create Cluster Servers**: Creates application servers within the specified ND cluster
2. **Configure Cluster**: Applies cluster-specific configuration settings
3. **Configure Node Servers**: Configures node servers after creation

## Notes

- Role is idempotent: safe to run multiple times
- Uses blocks and conditional logic for safe operations
- Ensure all required variables are set for your environment
- Cluster and servers must be named according to your WebSphere topology

## IBM Documentation

- [Creating cluster members](https://www.ibm.com/docs/en/was-nd/9.0.5?topic=clusters-creating-cluster-members)
- [Cluster concepts](https://www.ibm.com/docs/en/was-nd/9.0.5?topic=concepts-cluster)
- [Node agent management](https://www.ibm.com/docs/en/was-nd/9.0.5?topic=agents-node-agent-management)

## License

N/A
