# SeqWare 
#
# VERSION               1.1.0-alpha.6 
#
# Setup prerequities to run seqware-bag in order to setup a full SeqWare stack

FROM ubuntu:14.04
MAINTAINER Denis Yuen <denis.yuen@oicr.on.ca>

# use ansible to create our dockerfile, see http://www.ansible.com/2014/02/12/installing-and-building-docker-with-ansible
RUN apt-get -y update ;\
    apt-get install -y python-yaml python-jinja2 git wget sudo;\
    git clone http://github.com/ansible/ansible.git /tmp/ansible
WORKDIR /tmp/ansible
# get a specific version of ansible , add sudo to seqware, create a working directory
RUN git checkout v1.6.10 ;
ENV PATH /tmp/ansible/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
ENV ANSIBLE_LIBRARY /tmp/ansible/library
ENV PYTHONPATH /tmp/ansible/lib:$PYTHON_PATH
# setup seqware 
WORKDIR /root 
RUN git clone https://github.com/SeqWare/seqware-bag.git
COPY inventory /etc/ansible/hosts
WORKDIR /root/seqware-bag 
RUN git checkout 1.0.1-test 
ENV HOSTNAME master
# why is this required with Java 8 and local ansible connections??
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle
# hurray! this seems to satisfy gridengine-master's hostname lookup 
RUN echo "127.0.0.1    master" > /tmp/tmpfile && cat /etc/hosts >> /tmp/tmpfile
RUN cat /tmp/tmpfile > /etc/hosts && ansible-playbook seqware-install.yml -c local --extra-vars "seqware_version=1.1.1 docker=yes test_environment=yes seqware_provider=git"
# at this point, seqware has been fully setup
ENV HOME /home/seqware
USER seqware
WORKDIR /home/seqware
RUN git clone https://github.com/SeqWare/seqware-bag.git
# setup an ansible script to startup our required services when the container starts
RUN cd seqware-bag && git checkout 1.0.1-test

COPY ./scripts/start.sh /start.sh
RUN sudo chmod a+x /start.sh
COPY ./scripts/test-start.sh /test-start.sh
RUN sudo chmod a+x /test-start.sh

# setup docker in docker functionality assuming socket binding, inspired by https://github.com/jpetazzo/dind and https://github.com/docker/docker/issues/7285
# example command: docker run --privileged  -h master --rm -t -i -v /var/run/docker.sock:/var/run/docker.sock seqware/seqware_whitestar

#USER root
#RUN apt-get update -qq && apt-get install -qqy \
#    apt-transport-https \
#    ca-certificates \
#    curl \
#    lxc \
#    iptables
# Install Docker from Docker Inc. repositories.
#RUN curl -sSL https://get.docker.com/ | sh
# Add non-root access to docker
#RUN sudo gpasswd -a seqware docker

USER seqware
CMD ["/bin/bash", "/start.sh"]
