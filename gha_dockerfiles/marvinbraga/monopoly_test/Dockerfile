FROM python:3.9.2

ENV PYTHONUNBUFFERED=1
ENV PIPENV_VENV_IN_PROJECT=1
ENV PIPENV_IGNORE_VIRTUALENVS=1

WORKDIR /var/app

COPY . ./

RUN python3 -m pip install --upgrade pip \
    && pip3 install pipenv \
    && pipenv sync

CMD ["pipenv", "run", "python3", "main.py"]
