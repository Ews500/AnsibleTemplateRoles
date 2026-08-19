# was_create_standalone_profile

Create a WebSphere Application Server standalone profile.

## Requirements

- WebSphere Application Server must be installed
- webadmn user must exist
- Vault file must contain admin credentials

## Role Variables

### Required Variables
| Variable | Description | Example |
|----------|-------------|---------|
| `app` | Profile name to create | `amtreports` |
| `env_code` | Environment code | `FATW` |

### Default Variables

Check roles/was_create_standalone_profile/vars/main.yml file for default values.


## Dependencies

- `was_install`: WebSphere must be installed first

## Tags

- `check_profile`: Check if the profile already exists
- `create_profile`: Create the standalone profile
- `config_profile`: Configure the standalone profile
- `config_resources`: Configure resources for the profile


## Tasks Performed

1. **Check Profile**: Verifies WebSphere is installed
2. **Create Profile**: Uses manageprofiles.sh to create standalone profile
3. **Configure Profile**: Applies basic configuration settings
4. **Configure Resources**: Sets up necessary resources for the profile

## Notes

- Profile creation can take some minutes
- Ensure sufficient disk space (1GB+)
- Profile will be owned by webadmn user
- Stores admin credentials in vault for security

## IBM Documentation

- [Creating profiles with the manageprofiles command](https://www.ibm.com/docs/en/was-nd/9.0.5?topic=line-creating-profiles-manageprofiles-command)
- [Profile concepts](https://www.ibm.com/docs/en/was-nd/9.0.5?topic=concepts-profile)

## License

N/A
