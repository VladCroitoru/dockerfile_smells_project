FROM python:2.7-alpine

COPY /mesos-cloudwatch-autoscale.py /mesos-cloudwatch-autoscale.py

RUN pip install requests boto3

CMD python /mesos-cloudwatch-autoscale.py