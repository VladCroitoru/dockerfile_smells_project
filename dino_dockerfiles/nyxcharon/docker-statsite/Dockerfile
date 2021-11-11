FROM debian:8.3
RUN apt-get update && apt-get install -y \
    git \
    make \
    gcc \
    automake \
    autoconf \
    python \
    && rm -rf /var/lib/apt/lists/*
RUN mkdir /code && cd /code && git clone  https://github.com/armon/statsite.git
COPY conf /configs
COPY bin/dual-sink /code/dual-sink
COPY bin/start /start
RUN cd /code/statsite && ./bootstrap.sh && ./configure && make && mv ./src/statsite /code/statsite/statsite
ENTRYPOINT /start
