FROM ubuntu:17.04
MAINTAINER jmcarbo <jmcarbo@gmail.com>

ENV SLURM_VER=16.05.10-2
#ENV SLURM_VER=17.02.2


# Create users, set up SSH keys (for MPI)
RUN useradd -u 2001 -d /home/slurm slurm
RUN useradd -u 6000 -ms /bin/bash ddhpc
ADD etc/sudoers.d/ddhpc /etc/sudoers.d/ddhpc
ADD home/ddhpc/ssh/config /home/ddhpc/.ssh/config
ADD home/ddhpc/ssh/id_rsa /home/ddhpc/.ssh/id_rsa
ADD home/ddhpc/ssh/id_rsa.pub /home/ddhpc/.ssh/id_rsa.pub
ADD home/ddhpc/ssh/authorized_keys /home/ddhpc/.ssh/authorized_keys
RUN chown -R ddhpc:ddhpc /home/ddhpc/.ssh/
RUN chmod 400 /home/ddhpc/.ssh/*

# Install packages
RUN apt-get update && apt-get -y  dist-upgrade
RUN apt-get install -y munge curl gcc make bzip2 supervisor python python-dev \
    libmunge-dev libmunge2 lua5.3 lua5.3-dev libopenmpi-dev openmpi-bin \
    gfortran vim python-mpi4py python-numpy python-psutil sudo psmisc \
    software-properties-common python-software-properties iputils-ping \
    openssh-server openssh-client libreadline6 libreadline6-dev

#libcr-dev blcr-testsuite blcr-util libcr0
RUN apt-get install -y tzdata
ENV TZ=Europe/Madrid 
RUN echo $TZ | tee /etc/timezone 
RUN dpkg-reconfigure --frontend noninteractive tzdata

# Download, compile and install SLURM
#RUN curl -fsL http://www.schedmd.com/downloads/latest/slurm-${SLURM_VER}.tar.bz2 | tar xfj - -C /opt/ && \
#    cd /opt/slurm-${SLURM_VER}/ && \
#    ./configure && make && make install
#ADD etc/slurm/slurm.conf /usr/local/etc/slurm.conf
#RUN apt-get install -y slurm-wlm
RUN apt-get install -y slurm-llnl

# Configure OpenSSH
# Also see: https://docs.docker.com/engine/examples/running_ssh_service/
ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile
RUN mkdir /var/run/sshd
RUN echo 'ddhpc:ddhpc' | chpasswd
# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
ADD etc/supervisord.d/sshd.conf /etc/supervisor/conf.d/sshd.conf


# Configure GlusterFS
# RUN add-apt-repository ppa:gluster/glusterfs-3.8 && \
#     apt-get update -y && \
#     apt-get install -y glusterfs-server
#
# RUN mkdir -p /data/ddhpc
# ADD etc/supervisord.d/glusterd.conf /etc/supervisor/conf.d/glusterd.conf


# Configure munge (for SLURM authentication)
ADD etc/munge/munge.key /etc/munge/munge.key
RUN mkdir /var/run/munge && \
    chown root /var/lib/munge && \
    chown root /etc/munge && chmod 600 /var/run/munge && \
    chmod 755  /run/munge && \
    chmod 600 /etc/munge/munge.key
ADD etc/supervisord.d/munged.conf /etc/supervisor/conf.d/munged.conf


# Add Containerpilot and set its configuration
ENV CONTAINERPILOT_VERSION 2.7.2
ENV CONTAINERPILOT file:///etc/containerpilot.json
#
RUN export CONTAINERPILOT_CHECKSUM=e886899467ced6d7c76027d58c7f7554c2fb2bcc \
    && export archive=containerpilot-${CONTAINERPILOT_VERSION}.tar.gz \
    && curl -Lso /tmp/${archive} \
         "https://github.com/joyent/containerpilot/releases/download/${CONTAINERPILOT_VERSION}/${archive}" \
    && echo "${CONTAINERPILOT_CHECKSUM}  /tmp/${archive}" | sha1sum -c \
    && tar zxf /tmp/${archive} -C /usr/local/bin \
    && rm /tmp/${archive} \
    && curl -sL https://github.com/sequenceiq/docker-alpine-dig/releases/download/v9.10.2/dig.tgz|tar -xzv -C /usr/local/bin/

# configuration files and bootstrap scripts
#ENV CONSUL_SNAPSHOT_FREQUENCY 1m

# Add singularity
RUN apt-get update
RUN apt-get -y install build-essential curl git sudo man vim autoconf libtool default-jdk
RUN apt-get -y install python
RUN git clone https://github.com/singularityware/singularity.git
RUN cd singularity && ./autogen.sh && ./configure --prefix=/usr/local && make && make install
#
# Add nextflow
RUN cd /usr/local/bin && curl -fsSL get.nextflow.io | bash
RUN chmod +rw /usr/local/bin/nextflow

ADD consul-template /usr/local/bin/consul-template
RUN chmod +x /usr/local/bin/consul-template

EXPOSE 22
