FROM python:2
ADD . /nibbler
WORKDIR  /nibbler
RUN pip install -r requirements.txt

ENTRYPOINT python slave-collect.py --slave $SLAVE --influxdb-name $INFLUXDB_NAME --influxdb-host $INFLUXDB_HOST --influxdb-user $INFLUXDB_USER --influxdb-password $INFLUXDB_PASSWORD
