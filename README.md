

\# DevOps Core Tooling



!\[CI](https://github.com/Shaggu1234/devops-core-tooling/actions/workflows/ci.yml/badge.svg)

!\[License](https://img.shields.io/github/license/Shaggu1234/devops-core-tooling)



A Python-based project demonstrating Git version control, collaborative development, automated code quality checks, and CI workflows using GitHub Actions.



\## Table of Contents



\- \[Project Overview](#project-overview)

\- \[Architecture](#architecture)

\- \[Features](#features)

\- \[Prerequisites](#prerequisites)

\- \[Installation](#installation)

\- \[Environment Setup](#environment-setup)

\- \[Usage](#usage)

\- \[Testing](#testing)

\- \[CI Pipeline](#ci-pipeline)

\- \[Contribution Guidelines](#contribution-guidelines)

\- \[License](#license)



\## Project Overview



DevOps Core Tooling is a sample Python project created to demonstrate professional software engineering practices.



It includes application modules, configuration management, automated testing, GitHub collaboration, and continuous integration.



\## Architecture



The project follows a simple development and validation workflow.



```text

Developer

&#x20;  |

&#x20;  v

Git Feature Branch

&#x20;  |

&#x20;  v

GitHub Pull Request

&#x20;  |

&#x20;  v

GitHub Actions CI

&#x20;  |

&#x20;  +----> Flake8 Code Quality

&#x20;  |

&#x20;  +----> Pytest Unit Testing

&#x20;  |

&#x20;  v

Code Review and Merge

&#x20;  |

&#x20;  v

Main Branch

```



\## Features



\- Python application modules.

\- Authentication and logging examples.

\- Centralized application configuration.

\- User dashboard functionality.

\- Automated unit testing with pytest.

\- Code quality checks using flake8.

\- GitHub Actions CI integration.



\## Prerequisites



Install the following software:



\- Python 3.11 or later.

\- Git.

\- Git Bash or a terminal.

\- GitHub account.



\## Installation



Clone the repository:



```bash

git clone https://github.com/Shaggu1234/devops-core-tooling.git

```



Navigate to the project directory:



```bash

cd devops-core-tooling

```



Install dependencies:



```bash

python -m pip install -r requirements.txt

```



\## Environment Setup



Verify the Python installation:



```bash

python --version

```



Verify Git:



```bash

git --version

```



Install the project dependencies before running the application or tests.



\## Usage



Run the main application:



```bash

python main.py

```



Run the dashboard module:



```bash

python dashboard.py

```



Example dashboard function:



```python

from dashboard import get\_user\_dashboard



result = get\_user\_dashboard("Admin")

print(result)

```



\## Testing



Execute the unit tests:



```bash

python -m pytest -v

```



Run the code quality check:



```bash

python -m flake8 . --count --max-line-length=127 --statistics

```



\## CI Pipeline



GitHub Actions automatically validates code changes when:



\- Code is pushed to the main branch.

\- A Pull Request targets the main branch.



The pipeline performs:



1\. Repository checkout.

2\. Python environment setup.

3\. Dependency installation.

4\. Flake8 linting.

5\. Pytest unit testing.



\## Contribution Guidelines



Contributions are welcome.



1\. Create a feature branch.

2\. Implement your changes.

3\. Run linting and unit tests.

4\. Commit changes using descriptive commit messages.

5\. Open a Pull Request against main.

6\. Address review feedback before merging.



Refer to \[CONTRIBUTING.md](CONTRIBUTING.md) for contribution instructions and the \[Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/1/code\_of\_conduct/) for community standards.



\## License



This project is licensed under the MIT License. See \[LICENSE](LICENSE) for details.



