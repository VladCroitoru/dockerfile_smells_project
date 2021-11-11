FROM buildpack-deps:stretch

RUN apt-get update && apt-get install -y --no-install-recommends \
libasound2-dev \
libcups2-dev \
libxtst-dev \
openjdk-8-jdk \
unzip \
zip \
&& rm -rf /var/lib/apt/lists/*

RUN useradd -u 1000 -m docker
USER docker
