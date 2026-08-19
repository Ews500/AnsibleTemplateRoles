# was_monitoring

Configure monitoring for IBM WebSphere Application Server environments. This role sets up monitoring scripts, configures health checks, and integrates with external monitoring systems to ensure WebSphere services are running and healthy.

## Requirements

- WebSphere Application Server must be installed
- Sufficient privileges to deploy monitoring scripts and configure checks
- Monitoring endpoints and credentials (if integrating with external systems)

## Role Variables

### Required Variables

None


## Dependencies

None

## Tasks Performed

1. **Setup Monitoring**: Copy monitor_url script to host
2. **Configure NRPE**: Configure NRPE checks to verify WebSphere services are running
3. **Add URLs**:  Add URLs to the monitoring file

## Notes

- Role is idempotent: safe to run multiple times
- Supports custom monitoring scripts and endpoints
- Can be extended for integration with enterprise monitoring solutions
- Ensures proactive detection of service issues

## IBM Documentation

- [Monitoring WebSphere Application Server](https://www.ibm.com/docs/en/was-nd/9.0.5?topic=server-monitoring)
- [Health management](https://www.ibm.com/docs/en/was-nd/9.0.5?topic=management-health)

## License

N/A
