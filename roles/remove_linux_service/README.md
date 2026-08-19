# Remove Linux Service Role

This Ansible role removes systemd services for WebSphere Application Server standalone instances.

## Playbook Location

The main playbook `was_remove_linux_service.yml` is located in the repository root directory.

## Description

The `remove_linux_service` role safely removes systemd service files, stops running services, and cleans up associated sudo permissions for WebSphere Application Server standalone instances.

## Conditions

This role only operates when the `app` variable is **NOT** one of the following:
- `dmgr` (Deployment Manager)
- `nd` (Network Deployment/NodeAgent) 
- `ihs` (IBM HTTP Server)

For standalone application servers, it removes services named: `was_{{ env_code | lower }}{{ app_vars.common_app_group | default(app | lower) }}.service`

## What it does

1. **Stops and disables** the systemd service
2. **Removes** the service unit file from `/etc/systemd/system/`
3. **Cleans up** sudo permissions from `/etc/sudoers.d/03-webteam` and `/etc/sudoers.d/04-opsteam`
4. **Reloads** systemd daemon
5. **Verifies** service removal

## Variables

### Required Variables
- `app`: Application identifier (e.g., 'policyentity', 'invoicedp', etc.)
  - Usually passed via command line: `-e "app=policyentity"`
  - Or defined in playbook/inventory context
- `env_code`: Environment code (e.g., 'PROD', 'FATW', etc.)
  - Typically defined in group_vars/all.yml for each environment

### Optional Variables  
- `app_vars.common_app_group`: Alternative service name component (overrides `app` in service naming)
  - Loaded from app_vars files (e.g., app_vars/cabrillo.yml)
  - If not defined, `app` variable is used for service naming
  - Accessed as `app_vars.common_app_group` in templates and tasks

## Example Usage

### Command line usage:
```bash
# Remove service for policyentity app in FATW environment
ansible-playbook -i environments/FATW/hosts was_remove_linux_service.yml -e "app=policyentity"

# Remove service for invoicedp app in PROD environment  
ansible-playbook -i environments/PROD/hosts was_remove_linux_service.yml -e "app=invoicedp"
```

### In a playbook:
```yaml
- hosts: "{{ app | default('null') }}"
  tasks:
    - name: Include remove_linux_service role
      ansible.builtin.include_role:
        name: remove_linux_service
```

### With tags:
```yaml
- hosts: "{{ app | default('null') }}"
  tasks:
    - name: Include remove_linux_service role
      ansible.builtin.include_role:
        name: remove_linux_service
      tags: remove_service
```

## Service Names

The role removes services following this naming pattern:
- **Standalone servers**: `was_{{ env_code | lower }}{{ app_vars.common_app_group | default(app | lower) }}.service`

Examples:
- `was_prodpolicyentity.service` (PROD environment, app=policyentity, no app_vars.common_app_group → uses app | lower)
- `was_fatwinvoicedp.service` (FATW environment, app=invoicedp, no app_vars.common_app_group → uses app | lower)
### "cabrillo" has same profile as "reinsurance". Linux service was created only for "reinsurance" so we need to use app_vars.common_app_group.
- `was_prodreinsurance.service` (PROD environment, app=cabrillo, app_vars.common_app_group=reinsurance) 

### Service Name Logic:
1. If `app_vars.common_app_group` is defined → uses `app_vars.common_app_group` 
2. If `app_vars.common_app_group` is not defined → falls back to `app | lower` (ensures lowercase)

## Safety Features

- **Conditional execution**: Only runs for appropriate app types
- **Failed_when: false**: Won't fail if service doesn't exist
- **Debug output**: Shows what actions were taken
- **Verification**: Confirms service removal was successful

## Prerequisites

- Target hosts must be Linux with systemd
- Ansible user must have sudo privileges
- Services should be stopped before removal (role handles this)

## Tags

The role supports the following tags for selective execution:

- `remove_service` - Complete service removal process (all blocks)
- `pre_checks` - Pre-removal validation and status checks
- `systemd` - SystemD service operations (stop/disable/remove/reload)
- `verification` - Post-removal verification and cleanup
- `always` - Debug output and skip messages (always run)

### Usage Examples:
```bash
# Run everything (default)
ansible-playbook -i environments/FATW/hosts was_remove_linux_service.yml -e "app=invoicedp"

# Run only the role (skip playbook pre/post tasks)
ansible-playbook -i environments/FATW/hosts was_remove_linux_service.yml -e "app=invoicedp" --tags "remove_service"

# Run only pre-checks
ansible-playbook -i environments/FATW/hosts was_remove_linux_service.yml -e "app=invoicedp" --tags "pre_checks"

# Run only systemd operations (skip checks and verification)
ansible-playbook -i environments/FATW/hosts was_remove_linux_service.yml -e "app=invoicedp" --tags "systemd"

# Run only verification and cleanup
ansible-playbook -i environments/FATW/hosts was_remove_linux_service.yml -e "app=invoicedp" --tags "verification"

# Run pre-checks and systemd operations (skip verification)
ansible-playbook -i environments/FATW/hosts was_remove_linux_service.yml -e "app=invoicedp" --tags "pre_checks,systemd"

# Show only debug output and validation
ansible-playbook -i environments/FATW/hosts was_remove_linux_service.yml -e "app=invoicedp" --tags "always"
```

## Author

Atradius Web Management Team
