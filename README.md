# Edf Focus List
This project is used to load Focus List information in EDF.

## Requirements

* Python 3.9.12 (https://www.python.org/)
* Python Version Management: pyenv (https://github.com/pyenv/pyenv)
* PostgreSQL Client (For Ubuntu: https://www.postgresql.org/download/linux/ubuntu/)

Optionally (if isn't already installed):
Run ```sudo apt install libpq-dev``` to avoid ```libpq-fe.h``` error.

## Development configuration (on Mac M1)

### Install
* Install pyenv
```shell
brew update
# [if zlib is not installed yet]
# brew install zlib
# don't miss set up the environment variables in your shell profile
brew install pyenv
brew upgrade pyenv
pyenv init
# don't miss source shell rc
```

* Install Python 3.9.12
```shell
pyenv install 3.9.12
# [optional]
# pyenv global 3.9.12
```

* Create the environment, go to the project root and run:
```shell
pyenv local 3.9.12
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements-dev.txt
pip install -r requirements.txt
```

* Install pre-commit
```shell
pre-commit install
```

* Create virtual env with dependencies installed
```shell
pyenv local 3.9.12
python -m venv .venv
source .venv/bin/activate
```

* Run flake8 linter
```shell
pre-commit run --all-files
```


### Run
