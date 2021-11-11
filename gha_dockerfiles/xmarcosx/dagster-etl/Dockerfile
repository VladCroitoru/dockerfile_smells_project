FROM python:3.8-slim

ENV PYTHONUNBUFFERED=True
ENV DAGSTER_HOME=/opt/dagster/dagster_home
ENV DAGSTER_GRPC_MAX_RX_BYTES=20000000
ENV DBT_PROFILES_DIR=/opt/dagster/app
ENV DBT_PROJECT_DIR=/opt/dagster/app/alcozer_dbt
ENV PYTHONPATH=/opt/dagster/app/alcozer
ENV PYTHONWARNINGS=ignore

RUN mkdir -p /opt/dagster/dagster_home /opt/dagster/app

COPY requirements.txt /opt/dagster/app/
WORKDIR /opt/dagster/app
RUN pip install -r requirements.txt

COPY workspace.yaml /opt/dagster/app/
COPY alcozer /opt/dagster/app/alcozer
COPY alcozer_dbt /opt/dagster/app/alcozer_dbt
COPY profiles.yml /opt/dagster/app/
COPY dagster-prod.yaml /opt/dagster/dagster_home/dagster.yaml

COPY run-prod.sh /opt/dagster/app/
RUN ["chmod", "+x", "/opt/dagster/app/run-prod.sh"]

EXPOSE 3000

ENTRYPOINT ["/opt/dagster/app/run-prod.sh"]
