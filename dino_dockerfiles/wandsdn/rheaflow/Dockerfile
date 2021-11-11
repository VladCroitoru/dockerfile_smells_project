FROM osrg/ryu

RUN \
  apt-get update && \
  apt-get install -qy --no-install-recommends \
    python-pip supervisor iproute2 openvswitch-switch

COPY ./ /rheaflow-src/
COPY etc/supervisor/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN \
  pip install /rheaflow-src

RUN ovsdb-tool create /etc/openvswitch/conf.db /usr/share/openvswitch/vswitch.ovsschema
RUN mkdir /var/run/openvswitch/

VOLUME ["/usr/local/etc/ryu/"]

WORKDIR /usr/local/lib/python2.7/dist-packages/rheaflow

EXPOSE 6633

CMD ["/usr/bin/supervisord"]
