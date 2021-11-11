FROM ubuntu:trusty

MAINTAINER Sreeprakash Neelakantan <sree@schogini.com>

ENV PUPPET_AGENT_VERSION="5.1.0" UBUNTU_CODENAME="xenial" DUMB_INIT_VERSION="1.2.0" PUPPETSERVER_JAVA_ARGS="-Xms256m -Xmx256m" PATH=/opt/puppetlabs/server/bin:/opt/puppetlabs/puppet/bin:/opt/puppetlabs/bin:$PATH PUPPET_HEALTHCHECK_ENVIRONMENT="production"

RUN apt-get update && \
    apt-get install --no-install-recommends -y tree nano wget ca-certificates lsb-release && \
    wget https://apt.puppetlabs.com/puppetlabs-release-pc1-trusty.deb && \
    dpkg -i puppetlabs-release-pc1-trusty.deb && \
    apt-get update && \
    apt-get install --no-install-recommends -y puppet-agent && \
    apt-get install --no-install-recommends -y puppetserver 

RUN sed -i 's/Xms2g/Xms256m/'  /etc/default/puppetserver && \
    sed -i 's/Xmx2g/Xmx256m/'  /etc/default/puppetserver

RUN /opt/puppetlabs/bin/puppet resource service puppetserver ensure=running enable=true

RUN echo "PATH=/opt/puppetlabs/bin:\$PATH;export PATH;" >> /root/.bashrc

COPY ./code /etc/puppetlabs/code
COPY Dockerfile /

#docker build -t schogini/puppetserver-ubuntu .
#docker run -ti --rm --net puppet --name puppet --hostname puppet -v $PWD/code:/etc/puppetlabs/code/ schogini/puppetserver-ubuntu
