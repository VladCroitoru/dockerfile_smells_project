FROM python:2

# Not sure if python-protobuf is required, doesn't seem to work
RUN apt-get update && apt-get install python-protobuf protobuf-compiler wget -y

RUN pip install protobuf

RUN wget https://github.com/frymaster/eve-bot/archive/master.tar.gz -O /tmp/eve-bot.tar.gz && \
    tar -xf /tmp/eve-bot.tar.gz -C /tmp && \
    mv /tmp/eve-bot-master /opt/eve

RUN cd /opt/eve && \
    protoc --python_out=. Mumble.proto

WORKDIR /opt/eve

ENTRYPOINT ["python", "eve-bot.py"]
