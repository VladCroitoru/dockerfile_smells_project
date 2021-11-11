FROM ubuntu:trusty

RUN apt-get update
RUN apt-get install -y libyaml-0-2 libyaml-dev git subversion curl
RUN apt-get install -y python2.7-minimal python2.7-dev python-virtualenv python-pip
RUN apt-get install -y rbenv bundler
RUN apt-get install -y autoconf bison build-essential libssl-dev libyaml-dev libreadline6-dev zlib1g-dev libncurses5-dev libffi-dev libgdbm3 libgdbm-dev
RUN git clone https://github.com/sstephenson/ruby-build.git /root/.rbenv/plugins/ruby-build

RUN rbenv install 1.8.7-p375
RUN rbenv install 2.1.5

RUN mkdir -p /usr/omni

WORKDIR /work
COPY ansible /work/ansible
COPY puppet /work/puppet
COPY setup.sh /work/
RUN ./setup.sh ansible 1.0
RUN ./setup.sh ansible 1.8.4
RUN ./setup.sh puppet 3.2.4
RUN ./setup.sh puppet 3.4.3
RUN ./setup.sh puppet 3.7.5
RUN ./setup.sh puppet 4.0.0
RUN ./setup.sh puppet 4.1.0
RUN ./setup.sh puppet 4.2.0
RUN ./setup.sh puppet 4.2.1

COPY test.sh /work/test.sh
COPY bin/omni /usr/bin/omni
CMD ["/work/test.sh"]
