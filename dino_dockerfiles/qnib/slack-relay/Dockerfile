FROM qnib/consul
MAINTAINER "Christian Kniep <christian@qnib.org>"

RUN yum install -y python-pip unzip python-setuptools gcc python-devel
RUN pip install twisted requests envoy
ADD etc/supervisord.d/slack-relay.ini /etc/supervisord.d/slack-relay.ini
ADD opt/qnib/bin/start_slack-relay.py /opt/qnib/bin/
ADD relay.py /opt/qnib/slack-relay/


