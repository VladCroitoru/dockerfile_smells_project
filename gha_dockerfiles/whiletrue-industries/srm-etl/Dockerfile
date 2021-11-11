FROM akariv/dgp-app:395a2c0bad5cb84ef74d76ace3196e2d93a3c13a

USER etl

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY configuration.json dags/
COPY logo.png ui/dist/ui/en/assets/logo.png
COPY favicons/* ui/dist/ui/

COPY logo.png site/static/assets/img/logo.png

COPY events dags/events
COPY operators dags/operators/
COPY srm_tools srm_tools
COPY conf conf

ENV AIRFLOW__CORE__LOG_FORMAT="%(asctime)s:%(levelname)-8s:%(name)s:%(message)s"

COPY srm_etl_entrypoint.sh /app/
ENTRYPOINT ["/app/srm_etl_entrypoint.sh"]
