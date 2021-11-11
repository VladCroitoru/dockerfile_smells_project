FROM debian
MAINTAINER Ando Roots <ando@sqroot.eu>

RUN apt-get update && \
  DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends namebench && \
  rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["namebench", "-x"]
