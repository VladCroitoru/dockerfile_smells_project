FROM python:3.9-bullseye

WORKDIR /app

RUN pip install --upgrade pip pipenv

COPY . /app

RUN pipenv install

ENTRYPOINT [ "pipenv", "run", "server" ]