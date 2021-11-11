FROM python:3.9-alpine

WORKDIR /data

RUN apk add curl gcc musl-dev

COPY poetry.lock poetry.toml pyproject.toml /data/

ENV GET_POETRY https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py

RUN curl -sSL ${GET_POETRY} | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

COPY . .

RUN ls -l /data/reboot_notifier

RUN poetry install

ENTRYPOINT [ "notify-reboot" ]
