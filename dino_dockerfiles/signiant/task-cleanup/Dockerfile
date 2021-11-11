FROM jfloff/alpine-python:2.7-slim

MAINTAINER Signiant DevOps <devops@signiant.com>

ADD task_cleanup.py /task_cleanup.py

RUN pip install boto3 pytz
RUN chmod a+x /task_cleanup.py

ENTRYPOINT ["python", "/task_cleanup.py"]

CMD ["--help"]
