FROM ubuntu:16.04

RUN apt-get update && \
    apt-get install -y python3 python3-pip

RUN python3 -m pip install flask==0.12.2 h2==2.6.2

RUN mkdir -p /server
ADD mock-fcm-http2-server.py /server
ADD asyncio-http2-wsgi-server.py /server
ADD requirements.txt /server

EXPOSE 443 2197
ENTRYPOINT ["/server/asyncio-http2-wsgi-server.py", "mock-fcm-http2-server:app"]
