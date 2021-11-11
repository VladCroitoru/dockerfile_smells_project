FROM python:3

ADD run.sh /run.sh

RUN pip3 install docker jenkins-job-builder
RUN chmod +x /run.sh && mkdir -p /data && chmod 777 /data

VOLUME ["/data"]

ENTRYPOINT ["/run.sh"]
