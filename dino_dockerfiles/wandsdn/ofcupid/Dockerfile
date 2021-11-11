FROM osrg/ryu

RUN \
  apt-get update && \
  apt-get install -qy --no-install-recommends python-yaml

COPY ./ /ofcupid-src/

VOLUME ["/etc/ryu/ofcupid/"]

WORKDIR /ofcupid-src/

EXPOSE 6653 8080

CMD ["ryu-manager", "--ofp-tcp-listen-port=6653", "ofcupid.py"]
