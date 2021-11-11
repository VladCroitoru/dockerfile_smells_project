
FROM python:3-alpine

ADD . /gracc-request
WORKDIR /gracc-request
RUN pip install -r requirements.txt
RUN python setup.py install



RUN install -d -m 0755 /etc/graccreq/config.d/ && install -m 0744 config/gracc-request.toml /etc/graccreq/config.d/gracc-request.toml

CMD /usr/local/bin/graccreq

