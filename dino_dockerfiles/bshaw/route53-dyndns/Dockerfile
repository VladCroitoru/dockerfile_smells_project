FROM python:3-alpine

COPY . /opt/r53dyndns
WORKDIR /opt/r53dyndns
RUN pip3 install -r requirements.txt
ENTRYPOINT ["/opt/r53dyndns/run.sh"]
