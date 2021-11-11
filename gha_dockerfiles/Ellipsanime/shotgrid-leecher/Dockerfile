FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

ENV MODULE_NAME="shotgrid_leecher.main"

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

COPY ./poetry.toml /app/
COPY ./pyproject.toml /app/
COPY ./shotgrid_leecher /app/shotgrid_leecher

WORKDIR /app
RUN poetry export -f requirements.txt \
    --output requirements.txt \
    --without-hashes
RUN pip install -r requirements.txt
