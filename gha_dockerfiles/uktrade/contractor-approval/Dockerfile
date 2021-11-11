FROM python:3.9-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install poetry

ENV POETRY_VIRTUALENVS_CREATE=false

COPY poetry.lock pyproject.toml /app/

RUN poetry install

COPY . /app/

CMD python manage.py runserver 0.0.0.0:8000
