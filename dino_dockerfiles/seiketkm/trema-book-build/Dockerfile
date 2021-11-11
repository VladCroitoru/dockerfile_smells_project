FROM ubuntu:16.04
RUN apt-get update && apt-get install -y git ruby-dev openjdk-8-jdk rake ruby-bundler build-essential fonts-vlgothic && rm -rf /var/lib/apt/lists/*
VOLUME /data
ADD build.sh /
WORKDIR /trema-book
ENTRYPOINT ["/bin/bash", "/build.sh"]
