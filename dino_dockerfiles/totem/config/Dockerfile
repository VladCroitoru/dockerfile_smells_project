FROM totem/python-base:2.7-trusty-b3

ADD requirements.txt /opt/
RUN pip install -r /opt/requirements.txt

ADD . /opt/configservice
RUN chmod -R +x /opt/configservice/bin

EXPOSE 9003

WORKDIR /opt/configservice

ENTRYPOINT ["/opt/configservice/bin/run.sh"]
