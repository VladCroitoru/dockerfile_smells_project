FROM python:3.6.3

EXPOSE 8089

ENV PYZMQ_VERSION="==16.0.2"

RUN pip install locustio boto3 pyzmq${PYZMQ_VERSION}

ADD . /locust

WORKDIR /locust

RUN chmod +x /locust/start.sh

CMD /locust/start.sh
