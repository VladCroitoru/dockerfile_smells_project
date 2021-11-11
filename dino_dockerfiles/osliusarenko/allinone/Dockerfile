FROM debian:stable-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    python2.7 python-numpy python-scipy && \
    apt-get clean && rm -r /var/cache/apt/archives/*
RUN mkdir /calc

COPY [ "*.py", "/calc/" ]
COPY startscript.sh .

VOLUME [ "/calc/out/" ]

ENTRYPOINT [ "./startscript.sh" ]
