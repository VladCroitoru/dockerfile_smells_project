FROM python:3.5
MAINTAINER Artem Alexandrov

ENV REFRESHED 2018021801

RUN cd /opt && \
        git clone https://github.com/qk4l/cp-ru-server && \
        pip install -r cp-ru-server/requirements.txt

VOLUME /config/

EXPOSE 9090
WORKDIR /opt/cp-ru-server
ENTRYPOINT ["python", "/opt/cp-ru-server/server.py"]
