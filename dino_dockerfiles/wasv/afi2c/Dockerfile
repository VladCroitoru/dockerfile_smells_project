FROM debian:latest as maker
RUN apt-get -y update && \
    apt-get -y install --no-install-recommends \
    	gcc \
		libc6-dev \
        make \
    && rm -rf /var/lib/apt/lists/*
RUN apt-get -y update && \
    apt-get -y install --no-install-recommends \
        libreadline-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/project
COPY . .
RUN make clean && make RELEASE=y TARGET=test run
RUN make RELEASE=y TARGET=linux && make clean

FROM debian:latest
RUN apt-get -y update && \
    apt-get -y install --no-install-recommends \
        libreadline7 \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /root
COPY --from=maker /usr/src/project/bin/linux /bin/afi2c
CMD ["/bin/afi2c"]
