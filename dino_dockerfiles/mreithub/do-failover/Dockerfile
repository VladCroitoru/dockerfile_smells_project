FROM python:3-alpine

RUN adduser user -D -g 'App user,,,'

COPY failover.py /

USER user

CMD /usr/local/bin/python3 /failover.py
