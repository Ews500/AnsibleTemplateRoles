# openjdk_install

Install OpenJDK Java Development Kit for WebSphere Application Server.

## Requirements

- Linux system with package manager (yum/dnf)
- Network access to package repositories
- Root privileges for package installation

## Role Variables

### Required Variables
| Variable | Description | Example |
|----------|-------------|---------|
| `java_version` | OpenJDK version to install | `11.0.24.0.8-2` |

### Default Variables
| Variable | Default | Description |
|----------|---------|-------------|
| `java_home` | `/app/openjdk` | JDK installation directory |
| `installables_mount` | `/nfstemp` | Directory for installable files |

## Dependencies

None

## Tasks Performed

1. **Environment Setup**: Configures directories for JAVA_HOME
2. **Unarchive JDK**: Extracts JDK files to the appropriate directory
3. **Set JDK symbolic link**: Sets symbolic link to JAVA_HOME/java

## Supported Java Versions

- OpenJDK 11

## Notes

- Installs JDK (development kit) not just JRE
- Configures system-wide Java environment
- Compatible with WebSphere Application Server requirements
- Automatically handles package dependencies

## License

N/A
