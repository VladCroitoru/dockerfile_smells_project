FROM python:3.6-alpine

COPY requirements.txt /opt/requirements.txt

RUN pip install -r /opt/requirements.txt

COPY src/describe_ec2_instances.py /opt/describe_ec2_instances.py

ENTRYPOINT [ "/opt/describe_ec2_instances.py" ]

