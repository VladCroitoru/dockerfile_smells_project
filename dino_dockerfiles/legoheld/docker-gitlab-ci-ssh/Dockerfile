FROM ubuntu
MAINTAINER Michael Heimann

# install ssh client
RUN apt-get update -y && apt-get install openssh-client -y && rm -rf /var/lib/apt/lists/*

ADD entrypoint.sh /

# run entrypoint that reads env variable etc.
ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]
