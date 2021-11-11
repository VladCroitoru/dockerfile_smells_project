# Copyright 2015 lavvy lab, All rights reserved.

FROM ubuntu:14.04
MAINTAINER lavvy , lavashonline@gmail.com
ENV SCRIPT https://raw.githubusercontent.com/lavvy/buildmachine/master/build.sh

#install needed applications
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get install -y python-software-properties software-properties-common supervisor curl wget \
    devscripts git nano python-pip dh-make
# install docker
#RUN curl -fsSL https://get.docker.com/ | sh

RUN mkdir -p /root
WORKDIR /root

#add supervisord conf
ADD ./supervisord.conf /etc/supervisor/conf.d/supervisord.conf

#run your custom script
RUN echo '#!/bin/sh\n \
sleep 10\n \
curl -s -L ${SCRIPT} | bash\n \
/usr/bin/supervisord' > /root/run.sh

RUN chmod +x /root/run.sh
ENTRYPOINT ["/root/run.sh"]
