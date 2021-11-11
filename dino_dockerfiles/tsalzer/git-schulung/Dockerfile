# Docker container to present slides

FROM ubuntu:trusty

MAINTAINER Till Salzer <till.salzer@isax.com>

# base system
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git-core build-essential golang

# the user
RUN adduser --uid 1000 -c "Slides Presentation User" user

# now, install all the required stuff into /home/user
USER 1000
WORKDIR /home/user
ENV GOPATH /home/user

ADD Makefile *.slide /home/user/

RUN make bin/present

# the default port is 3999
EXPOSE 3999

ADD run_present.sh /home/user/bin/run_present.sh

# CMD ["/bin/bash", "-c", "/home/user/bin/present", "-http=\$(head -1 /etc/hosts | cut -f 1):3999", "-play=false"]

CMD ["/bin/bash", "-c", "/home/user/bin/run_present.sh"]
