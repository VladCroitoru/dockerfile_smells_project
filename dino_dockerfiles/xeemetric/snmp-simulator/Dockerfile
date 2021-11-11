FROM python:2.7

MAINTAINER Dmitry Korobitsin <https://github.com/korobitsin>

COPY . /tmp/simulator/

RUN set -x \
    && pip install /tmp/simulator \
    && mv /tmp/simulator/tests/cisco_2801.walk / \
    && rm -rf /tmp/simulator

EXPOSE 161/udp

CMD ["snmp-simulator", "-s", "--host", "0.0.0.0", "--port", "161", "--walk_file", "cisco_2801.walk"]
