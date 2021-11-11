FROM totem/python-base:3.4-trusty-b2

# App dependencies
ADD requirements.txt /opt/requirements.txt
RUN pip3 install -r /opt/requirements.txt

ADD . /opt/mongo-connector/

WORKDIR /opt/mongo-connector

CMD ["/opt/mongo-connector/run.py"]
