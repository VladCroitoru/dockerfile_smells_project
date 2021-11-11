FROM python:2.7-alpine

WORKDIR /root

RUN pip install requests
RUN pip install influxdb

COPY plexpy_influxdb_export.py plexpy_influxdb_export.py 
COPY docker/run.sh run.sh

CMD ["./run.sh"]
