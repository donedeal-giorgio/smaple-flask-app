# Base code for a flask API with AWS CI/CD

This repository contain a boilerplate for CRUD ops 
using the python Flask framework.

## Installation and dev

```
git clone git@github.com:donedeal-giorgio/smaple-flask-app.git sample-flask-api
cd sample-flask-api
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip isntall -e .
python wsgi.py
```

Alternatively, run it as a docker container:

```
make build
make run
```
