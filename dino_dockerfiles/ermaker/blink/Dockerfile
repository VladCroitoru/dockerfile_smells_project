FROM ubuntu:trusty

RUN export DEBIAN_FRONTEND=noninteractive \
    && apt-get update \
    && apt-get install -y \
      netcat-traditional \
    && rm -rf /var/lib/apt/lists/* \
    && update-alternatives --set nc /bin/nc.traditional

EXPOSE 4225

COPY . .
CMD ./blink.sh
