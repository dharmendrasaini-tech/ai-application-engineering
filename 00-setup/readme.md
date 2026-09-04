# Phase 0 - Setup & Baseline 

Development environment setup, Python project environment basics, Git/GitHub Setup and baseline exercises.

## Phase 0 Covers

- **Development environment setup** -> Python, VS Code, Git, Docker, PostgreSQL, Homebrew

- **Python project environment basics** -> `venv`, `pip`, `requirements.txt`, `pyproject.toml`

- **Git/GitHub Setup** -> local Git repository, commits, remote GitHub repository

- **Baseline exercises** -> 5 easy Python problems solved independently


## 1. Development Environment

Tools used

- Python
- VS Code
- Homebrew
- Git
- Docker
- PostgreSQL

### Python

Check Python version:

```python3 --version```

- `python3` runs the Python 3 interpreter.
- `--version` displays the installed Python version.

Check Python path:

```which python3```

- `which python` shows the exact Python executable your Terminal is using.
- This is useful when multiple Python versions are installed.


### VS Code

Check VS Code version:

```code --version``` 

- `code --version` shows the current installed VS Code version.

- `code .` opens the current folder in VS Code.


### Homebrew

Check Homebrew version:

```brew --version```


Update Homebrew package information

```brew update```



Check Outdated packages:

```brew outdated```


Update Outdated packages:

```brew upgrade```

- Homebrew is a package manager for macOS. 
- `brew update` updates Homebrew and its package information.
- `brew outdated` shows installed packages that have newer versions available.
- `brew upgrade` upgrades outdated packages.


### Git

Check Git version

```git --version```

- It shows the installed Git version.

Git is a version-control system used to track changes in a project.



### Docker

Check Docker version

```docker --version```

```docker --version``` shows the installed Docker version.
- Docker is used to run application inside isolated containers.

Verify docker is working

```docker run hello-world```

- `docker run hello-world` checks that Docker can pull an image, create a container, and run it successfully.
- If it prints `Hello from Docker!`, Docker is working correctly.

Docker image
→ blueprint

Docker container
→ running instance of that image


### PostgreSQL

Check PostgreSQL version

```psql-version```

```psql-version``` shows the installed PostgreSQL client version.

It is a relational database system.

Verify PostgreSQL is running:

```pg_isready```


- `pg_isready` checks whether the PostgreSQL server is accepting connections.
- If it shows `accepting connections`, PostgreSQL is running correctly.


PostgreSQL
→ database server

psql
→ command-line tool used to communicate with PostgreSQL



## 2. Python Project Environment Basics

### Virtual Environment

A virtual environment creates an isolated Python environment for a project.

- It keeps project dependencies separate from other Python projects.


Create a virtual environment:

```python3 -m venv .venv```


- `python3` runs Python 3.
- `-m` runs a Python module as a program.
- `venv` is Python's built-in virtual environment module.
- `.venv` is the folder where the virtual environment is created.


Activate the virtual environment:

```source .venv/bin/active```

- `source` runs the activation script in the current Terminal session.
- After activation, the Terminal usually shows `(.venv)`.



Deactivate the virtual environment:

```deactivate```


- `deactivate` stops using the current virtual environment.
- It does not delete `.venv`; it only returns the Terminal to the normal Python environment.



create .venv
    ↓
activate
    ↓
use project Python
    ↓
deactivate
    ↓
return to normal shell Python


### pip 

Check pip version:

```python -m pip --version```

- `pip` installs and manages Python packages.
- `python -m pip` uses the pip linked to the current Python interpreter.


Install a package:

```python -m pip install requests```

- `pip install` downloads and installs a Python package
- `requests` is the package being installed


your project
   ↓
requests
   ↓
its dependencies


### requirements.txt

Create a requirements file:

```python -m pip freeze > requirements.txt```

- `pip freeze` lists installed packages with their versions.

- `>` writes that output into `requirements.txt`.

- `requirements.txt` helps recreate the same Python environment later.


### pyproject.toml


`pyproject.toml` stores project metadata and Python project configuration.
pyproject.toml is a configuration file for a Python project. Think of it as the project’s “identity + requirements + tool settings” file.

Example:

```toml
[project]
name = "ai-application-engineering"
version = "0.1.0"
requires-python = ">=3.14"

dependencies = [
    "requests>=2.34,<3",
]
```

- `name` is the project name.
- `version` is the project version.
- `requires-python` defines the supported Python version.
- `dependencies` lists the packages the project directly requires.



requirements.txt
→ "What exact packages are installed in this environment?"

pyproject.toml
→ "What does this project require/configure?"



## 3. Git/GitHub Setup

Git tracks project changes locally, while GitHub stores the repository online.


Initialize Git in the current project:


```git init```


- `git init` turns the current folder into a Git repository.
- It creates a hidden `.git` folder that stores Git repository data.


Check Git repository status:

```git status```

- `git status` shows the current state of the repository.
- It tells you which files are untracked, modified, or staged.


Untracked
→ Git sees the file but is not tracking it yet.

Modified
→ A tracked file has changed.

Staged
→ A change has been selected for the next commit.


Stage all current changes:


```git add .```


- `git add .` stages all current changes in the current project for the next commit.
- Staging means selecting which changes should be included in the next commit.


Save staged changes in Git history:


```git commit -m "initial setup"```


- `git commit` saves the staged changes as a checkpoint in Git history.
- `-m` lets you write the commit message directly in the command.

staged changes
    ↓
git commit
    ↓
saved checkpoint in local Git history


