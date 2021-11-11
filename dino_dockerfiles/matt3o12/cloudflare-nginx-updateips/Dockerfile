FROM python:3.4-slim

RUN pip install requests

RUN mkdir -p /usr/app/
COPY updateIPs.py /usr/app/
COPY help.txt /usr/app/

WORKDIR /usr/app/
ENTRYPOINT ["/usr/local/bin/python", "updateIPs.py"]

