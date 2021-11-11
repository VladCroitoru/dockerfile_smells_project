FROM python:3.9

WORKDIR /visiobas_gateway/

# Install ping
RUN apt-get update && apt-get install -y iputils-ping

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# Copy poetry.lock* in case it doesn't exist in the repo
COPY ./pyproject.toml ./poetry.lock* /visiobas_gateway/

RUN poetry install --no-dev

COPY ./visiobas_gateway /visiobas_gateway
EXPOSE 7070
ENV PYTHONPATH=/visiobas_gateway

CMD ["python", "/visiobas_gateway"]