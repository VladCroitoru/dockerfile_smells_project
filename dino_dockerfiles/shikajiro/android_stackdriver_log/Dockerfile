FROM python:2

RUN apt-get -y install gcc git \
    && pip install google-cloud-logging \
    && pip install git+https://github.com/shikajiro/xmppgcm

COPY xmpp.py /

ENTRYPOINT ["python", "/xmpp.py"]
