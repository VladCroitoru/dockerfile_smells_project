FROM python:3
ENV INTERVAL 5
ENV TAUTULLI_HOST localhost
ENV TAUTULLI_PORT 8181
ENV TAUTULLI_KEY NONE
ENV INFLUXDB_HOST localhost
ENV INFLUXDB_PORT 8086
ENV INFLUXDB_DB TAUTULLI
ADD plexpy_influxdb_export.py /
RUN pip install influxdb
CMD python /plexpy_influxdb_export.py --plexpyhost "$TAUTULLI_HOST" --plexpyport "$TAUTULLI_PORT" --plexpyapikey "$TAUTULLI_KEY" --interval "$INTERVAL" --influxdbhost "$INFLUXDB_HOST" --influxdbport "$INFLUXDB_PORT" --influxdbdatabase "$INFLUXDB_DB"
