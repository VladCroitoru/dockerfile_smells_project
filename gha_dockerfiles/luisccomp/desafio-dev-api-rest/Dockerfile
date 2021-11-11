FROM python:3.8.12

WORKDIR /usr/app

COPY requirements.txt requirements.txt
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN python -m venv venv
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv sync --system

COPY . .

EXPOSE 5000
