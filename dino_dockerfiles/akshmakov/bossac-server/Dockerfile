FROM akshmakov/bossa

#socat
RUN apt-get update -y && apt-get install -y socat && rm -rf /var/lib/apt/lists/*

COPY bossac-server.sh /usr/local/bin/bossac-server

ENTRYPOINT [ "bossac-server" ]

