FROM ubuntu:bionic
RUN apt-get update -qq && \
    apt-get install -yqq unbound wget

WORKDIR /
ADD src/prep.sh /prep.sh
ADD src/root.key /var/unbound/etc/
ADD src/unbound.conf /etc/unbound/unbound.conf
ADD src/anchor-resolv.conf /anchor-resolv.conf
ADD src/update-key.sh /update-key.sh
ADD src/entrypoint.sh /entrypoint.sh

RUN chmod +x /prep.sh /entrypoint.sh /update-key.sh
RUN /prep.sh

RUN apt-get -y autoremove && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

VOLUME ["/var/log/"]

EXPOSE 53
EXPOSE 53/UDP

ENTRYPOINT ["/entrypoint.sh"]
