FROM ubuntu
RUN  apt-get update \
  && apt-get install -y wget \
  && rm -rf /var/lib/apt/lists/* \
  && wget https://minergate.com/download/deb-cli -O minergate-cli.deb \
  && dpkg -i minergate-cli.deb && rm minergate-cli.deb

ENTRYPOINT ["minergate-cli"]
