FROM jfloff/alpine-python:2.7-slim

MAINTAINER Signiant DevOps <devops@signiant.com>

COPY ecs_cluster_scaledown.py /ecs_cluster_scaledown.py

RUN pip install boto3 pytz
RUN chmod a+x /ecs_cluster_scaledown.py

ENTRYPOINT ["python", "/ecs_cluster_scaledown.py"]

CMD ["--help"]
