from python:3
add Pipfile* /app/
workdir /app
env PIPENV_VENV_IN_PROJECT=1
run pip install -U pip pipenv && pipenv install --three
add . /app/
CMD [".venv/bin/python3", "app.py"]
