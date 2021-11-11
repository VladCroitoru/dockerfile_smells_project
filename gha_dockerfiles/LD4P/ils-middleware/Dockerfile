FROM apache/airflow:2.2.1-python3.9

ENV POETRY_VERSION=1.1.8

USER root
RUN apt-get -y update && apt-get -y install git
USER airflow

RUN pip install "poetry==$POETRY_VERSION"
COPY --chown=airflow:root poetry.lock pyproject.toml /opt/airflow/
COPY --chown=airflow:root ./ils_middleware /opt/airflow/ils_middleware

RUN poetry build --format=wheel
RUN pip install dist/*.whl
