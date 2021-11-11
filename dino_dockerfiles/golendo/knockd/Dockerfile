FROM ubuntu

RUN apt-get update && apt-get install -y iptables knockd

COPY entrypoint /
RUN chmod +x /entrypoint

ENTRYPOINT ["/entrypoint"]
