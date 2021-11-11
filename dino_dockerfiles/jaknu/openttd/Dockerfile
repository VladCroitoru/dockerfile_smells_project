FROM ubuntu:16.10

RUN apt -y update && apt -y install openttd && rm -r /var/lib/apt/lists/*

COPY openttd.cfg /root/.openttd/openttd.cfg
COPY serverstart.sh /serverstart.sh

EXPOSE 3979/tcp
EXPOSE 3979/udp

CMD ["/serverstart.sh"]

