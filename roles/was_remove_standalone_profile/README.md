# was_remove_standalone_profile

The `was_remove_standalone_profile` role will remove a Standalone Profile in WebSphere Application Server.

## Requirements

- Define application name in `environments/<env_code>/hosts` files. This name will be later used as `app` variable in the role.
- Include vault file for that particular environment (`environments/<env_code>/vault.yml`) to ensure all variables are loaded.
- `app_vars` (`environments/app_vars/<app>.yml`) and `env_vars` (`environments/<env_code>/group_vars/<app>.yml`) files must exist for the `app` profile that will be removed.

## Role Variables

| Variable       | Default | Required | Description                             |
|----------------|---------|----------|-----------------------------------------|
| `app`          | N/A     | Yes      | Application profile name to remove      |


## Dependencies

None

## Example Playbook

```
- name: Remove Standalone WebSphere Application Server Profile
  hosts: "{{ app | default('null') }}"
  tasks:
    - name: Remove Standalone Profile
      tags: always
      ansible.builtin.include_role:
        name: was_remove_standalone_profile
```

## IBM Deleting Profiles Documentation
- [Deleting Profiles](https://www.ibm.com/docs/en/was/9.0.5?topic=mpdios-deleting-profiles)

## License

N/A
