FROM mazzolino/armhf-ubuntu:14.04
#FROM ubuntu:14.04

# Use dev.sh to build and run this Dockerfile using
# the second FROM instruction instead of the first.


MAINTAINER Jostein Austvik Jacobsen

WORKDIR /home/root/

ADD src /home/root/src/

ENTRYPOINT ["/home/root/src/run.sh"]
