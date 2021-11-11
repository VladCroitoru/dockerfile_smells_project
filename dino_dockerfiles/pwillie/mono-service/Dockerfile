FROM pwillie/mono-runtime:5.14

# MAINTAINER Peter Wilson <pwillie@users.noreply.github.com>

RUN apt-get update && apt-get install -y --no-install-recommends \
    mono-4.0-service \
  && rm -rf /var/lib/apt/lists/* /tmp/*
