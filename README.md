# WebSphere Infrastructure as Code

This repository contains roles, playbooks and environments for ansible templating and learning


This repository contains Ansible playbooks and roles for automating IBM WebSphere Application Server installation, configuration, and application deployment for .

## Repository Structure

```
├── environments/          # Environment-specific configurations
│   ├── app_vars/         # Application-specific variables
│   ├── BAT/              # BAT (SYMG) environment
│   ├── FATF/             # FATF (SYMF) environment
│   ├── FATW/             # FATW (SYMW) environment
│   ├── PROD/             # PROD (SYMP) environment
│   └── RELS/             # RELS (SYMZ) environment
├── roles/                # Ansible roles for various WAS operations
├── collections/          # External collection requirements
└── *.yml                # Main playbooks
```

## Prerequisites

- Ansible 2.9+
- Python 3.6+
- SSH access to target servers


## Available Playbooks

| Playbook | Description | Usage |
|----------|-------------|-------|
| `was_deploy_application.yml` | Deploy applications to WebSphere | `ansible-playbook was_deploy_application.yml -e env_code=FATW -e app=amtreports` |
| `was_install.yml` | Install WebSphere Application Server | `ansible-playbook was_install.yml -e env_code=FATW` |
| `was_create_standalone_profile.yml` | Create standalone WAS profile | `ansible-playbook was_create_standalone_profile.yml -e env_code=FATW` |
| `was_create_nd_profile.yml` | Create Network Deployment profile | `ansible-playbook was_create_nd_profile.yml -e env_code=FATW` |
| `was_start_service.yml` | Start WebSphere services | `ansible-playbook was_start_service.yml -e env_code=FATW` |
| `was_stop_service.yml` | Stop WebSphere services | `ansible-playbook was_stop_service.yml -e env_code=FATW` |

## Quick Start

1. **Install dependencies:**
   ```bash
   ansible-galaxy install -r collections/requirements.yml
   ```

2. **Deploy an application:**
   ```bash
   ansible-playbook was_deploy_application.yml -e env_code=FATW -e app=amtreports
   ```

3. **Install WebSphere:**
   ```bash
   ansible-playbook was_install.yml -e env_code=FATW
   ```

## Environment Variables

- `env_code`: Target environment (FATW, FATF, BAT, RELS, PROD)
- `app`: Application name (must match file in `environments/app_vars/`)

## Security

Sensitive data is encrypted using Ansible Vault. Ensure your vault password is configured before running playbooks.

### Vault Management
```bash
# Encrypt a vault file
ansible-vault encrypt environments/FATW/vault.yml

# Edit an encrypted vault file
ansible-vault edit environments/FATW/vault.yml

# View an encrypted vault file
ansible-vault view environments/FATW/vault.yml
```

## Troubleshooting

### Common Issues
1. **Vault missing**: Ensure vault is loaded in the playbook
2. **Variable not found**: Verify variables for `app` exist in `environments/app_vars/`, `environments//group_vars/` and within environment vault

### Debugging
```bash
# Run with increased verbosity
ansible-playbook was_deploy_application.yml -e env_code=FATW -e app=amtreports -vvv

# Check syntax without execution
ansible-playbook was_deploy_application.yml --syntax-check

# Dry run to see what would change
ansible-playbook was_deploy_application.yml -e env_code=FATW -e app=amtreports --check --diff
```

## Contributing

1. Follow Ansible best practices
2. Update documentation for new roles/playbooks
3. Test changes in non-production environments first
4. Use semantic versioning for releases
