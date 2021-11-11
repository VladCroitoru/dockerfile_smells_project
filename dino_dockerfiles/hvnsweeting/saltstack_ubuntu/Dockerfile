FROM ubuntu:14.04
MAINTAINER Viet Hung Nguyen <hvn@familug.org>

ADD . /app
RUN apt-get update
RUN apt-get install -y curl
RUN curl https://repo.saltstack.com/apt/ubuntu/14.04/amd64/latest/SALTSTACK-GPG-KEY.pub | sudo apt-key add -
RUN echo "deb http://repo.saltstack.com/apt/ubuntu/14.04/amd64/latest trusty main" > /etc/apt/sources.list.d/saltstack.list
RUN apt-get update
RUN apt-get install -y salt-minion
RUN curl -Lo /tmp/master.tar.gz https://github.com/hvnsweeting/states/archive/master.tar.gz
RUN mkdir -p /root/salt/pillar
RUN curl -Lo /root/salt/pillar/common.sls https://gist.githubusercontent.com/hvnsweeting/d8143b10e02fff01c434/raw/fd98d1015522446ba3ecc8d3b0dd395de476a790/common.sls
RUN printf 'base:\n  "*":\n    - common\n' > /root/salt/pillar/top.sls
RUN cd /; tar xzf /tmp/master.tar.gz -C /root/salt
RUN mv /root/salt/states-master /root/salt/states
RUN salt-call -c /root/salt/states/test saltutil.sync_all
RUN salt-call -c /root/salt/states/test state.sls vim
