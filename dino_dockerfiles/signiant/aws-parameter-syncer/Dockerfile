FROM python:3.8-slim

MAINTAINER Signiant DevOps <devops@signiant.com>

RUN mkdir -p /credentials

ADD parameter_sync.py /parameter_sync.py
ADD parameter_sync.sh /parameter_sync.sh

RUN pip install boto3
RUN chmod a+x /parameter_sync.py /parameter_sync.sh

VOLUME /credentials

ENTRYPOINT ["/parameter_sync.sh"]
