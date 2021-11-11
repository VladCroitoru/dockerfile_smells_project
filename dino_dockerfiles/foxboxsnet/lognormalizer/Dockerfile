FROM ubuntu:17.10

LABEL maintainer="FoxBoxsnet"

RUN \
           apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y liblognorm-utils \
    \
    # Cleanup
    && rm -rf /var/lib/apt/lists/*

CMD [ "/bin/bash" ]
