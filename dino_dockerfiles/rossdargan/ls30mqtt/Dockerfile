FROM perl:latest

MAINTAINER Ross Dargan dockermaintainer@the-dargans.co.uk

WORKDIR /var/

RUN git clone https://github.com/nickandrew/LS30.git

WORKDIR /var/LS30

COPY script.py /var/LS30/

ENV PERLLIB $PERLLIB:/var/LS30/lib
ENV LS30_SERVER=127.0.0.1:1681

RUN cpanm Date::Format AnyEvent AnyEvent::MQTT

RUN apt-get update && apt-get install -y python3 python3-pip

RUN pip3 install paho-mqtt

CMD ["python3", "-u",  "script.py"]
