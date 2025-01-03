# piccolo_project

## Setup

### Install requirements

```bash
pip install -r requirements.txt
```

### Getting started guide

```bash
python main.py
```

### Running tests

```bash
piccolo tester run
```
### Database sync

```bash
alembic revision --autogenerate -m "<message>"
alembic upgrade head         
```