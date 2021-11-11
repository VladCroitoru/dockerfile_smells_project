## -*- docker-image-name: "saltmaster" -*-
FROM shift/ubuntu:15.04

MAINTAINER Vincent Palmer <shift@someone.section.me>

RUN apt-get update \
    && apt-get install git-core python-dev \
      libyaml-dev libffi-dev libssl-dev \
      libssh2-1-dev cmake pkg-config swig curl libtool autoconf libsodium-dev --yes --force-yes \
    && git clone https://github.com/libgit2/libgit2.git \
    && cd libgit2 \
    && git checkout v0.22.1 \
    && mkdir build \
    && cd build \
    && cmake .. \
    && make \
    && make install \
    && ldconfig \
    && cd ../.. \
    && rm -rf libgit2 \
    && git clone https://github.com/zeromq/libzmq.git \
    && cd libzmq \
    && mkdir build \
    && cd build \
    && cmake .. \
    && make \
    && make install \
    && cd \
    && rm -rf libzmq \
    && curl -O https://raw.githubusercontent.com/pypa/pip/1.5.6/contrib/get-pip.py \
    && python get-pip.py \
    && rm get-pip.py \
    && git clone https://github.com/saltstack/salt.git /opt/salt 
WORKDIR /opt/salt
RUN cd /opt/salt \
    && pip install -r requirements/base.txt \
    && pip install -r requirements/zeromq.txt
RUN pip install -r requirements/raet.txt \
    && pip install cffi pygit2==0.22.1 M2Crypto Mako msgpack_pure GitPython \
    && pip install -i https://pypi.binstar.org/pypi/simple python-etcd \
    && pip install python-gnupg \
    && git checkout origin/2015.8 \
    && python setup.py install \
    && mkdir -p /etc/salt /var/log/salt \
    && cp -av conf/* /etc/salt \
    && rm -rf /var/lib/apt/lists/* \
    && echo "Host github.com\n  IdentityFile /etc/salt/repo.key" \
    && ssh-keyscan -H github.com > /etc/ssh/ssh_known_hosts \
    && ssh-keyscan -H bitbucket.com >> /etc/ssh/ssh_known_hosts

VOLUME /etc/salt
VOLUME /srv/pillar
VOLUME /srv/salt
VOLUME /srv/reactor
VOLUME /var/log/salt
VOLUME /var/cache/salt

# ZeroMQ ports
EXPOSE 4505/tcp
EXPOSE 4506/tcp
# RAET port
EXPOSE 4506/udp

