FROM ubuntu:14.04
MAINTAINER nyxcharon@gmail.com

# Let's start with some basic stuff.
RUN apt-get update -qq && apt-get install -qqy \
    apt-transport-https \
    ca-certificates \
    curl \
    lxc \
    iptables \
    ruby

# Install Docker from Docker Inc. repositories.
RUN curl -sSL https://get.docker.com/ | sh

# Install the magic wrapper.
ADD ./wrapdocker /usr/local/bin/wrapdocker
RUN chmod +x /usr/local/bin/wrapdocker
ENV LOG=file

#Add the audit script
ADD ./dockerAudit.rb /usr/bin/docker-audit
RUN chmod +x /usr/bin/docker-audit

#Scripts folder for various test
ADD ./scripts /scripts

#Add lynis security suite
ADD ./lynis /lynis

# Define additional metadata for our image.
VOLUME /var/lib/docker
ENTRYPOINT ["wrapdocker"]
