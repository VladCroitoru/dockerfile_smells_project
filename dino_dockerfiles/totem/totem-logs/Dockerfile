FROM totem/python-base:2.7-trusty-b2

ENV DEBIAN_FRONTEND noninteractive

# App dependencies
ADD requirements.txt /opt/requirements.txt
RUN pip install -r /opt/requirements.txt

ADD . /opt/totem-logs
RUN pip install -r /opt/totem-logs/requirements.txt

EXPOSE 9500

WORKDIR /opt/totem-logs

ENTRYPOINT ["/usr/local/bin/gunicorn"]
CMD ["-b","0.0.0.0:9500","-k", "flask_sockets.worker","totemlogs.server:app"]