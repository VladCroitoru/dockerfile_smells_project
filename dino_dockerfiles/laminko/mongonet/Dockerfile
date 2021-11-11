# Just a mongodb image with some net utilities
# 2018-03-20 18:53

FROM mongo:latest
ENV HOME /root
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils \
    && apt-get update && apt-get install -y --no-install-recommends \
                dnsutils \
                iputils-ping \
                iputils-tracepath \
		net-tools \
                traceroute \
        && rm -rf /var/lib/apt/lists/*
