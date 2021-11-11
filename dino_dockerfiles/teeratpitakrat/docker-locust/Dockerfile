FROM python:2-alpine

RUN apk add --update alpine-sdk
RUN pip install locustio pyzmq influxdb

ENV SCENARIO_FILE /locustfile.py
ADD run.sh /usr/local/bin/run.sh
RUN chmod 755 /usr/local/bin/run.sh

EXPOSE 8089 5557 5558

CMD ["/usr/local/bin/run.sh"]
