# surfeasy/puppet_base
#
# VERSION 0.0.1

# Create a base image for puppetdb and puppetserver 
FROM ubuntu:14.04
MAINTAINER Siwei Wang <swang@surfeasy.com>

# Install dependency
RUN apt-get update && apt-get install -y wget dnsutils

# Setup coreDNS dirs
RUN mkdir /coreDNS
WORKDIR /coreDNS

# Install coreDNS version v002
RUN wget https://github.com/miekg/coredns/releases/download/v002/coredns_002_linux_x86_64.tgz && tar xvzf coredns_002_linux_x86_64.tgz

# Add configuration
ADD . .

# Expose ports
EXPOSE 53

CMD ["./coredns",  "-log",  "stdout",  "-conf", "Corefile"]
