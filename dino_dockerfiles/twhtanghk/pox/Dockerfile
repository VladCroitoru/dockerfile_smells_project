FROM python:2-slim

WORKDIR /usr/src/app
ADD https://github.com/twhtanghk/pox/archive/eel.tar.gz /tmp
RUN tar --strip-components=1 -xzf /tmp/eel.tar.gz && \
        rm /tmp/eel.tar.gz
        
ENTRYPOINT ./pox.py l3_switch --fakeways=192.168.64.2 info.packet_dump log.level --DEBUG
