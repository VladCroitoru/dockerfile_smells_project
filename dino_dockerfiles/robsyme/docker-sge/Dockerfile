# Dockerfile to build SGE enabled container 

# Cloned and updated version of the docker-sge container from gawbul

FROM phusion/baseimage:0.9.19

# expose ports
EXPOSE 6444
EXPOSE 6445
EXPOSE 6446

# set environment variables
ARG HOME=/root

# regenerate host ssh keys
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh

# install required software
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update -y \
    && apt-get install -y sudo bsd-mailx tcsh db5.3-util libhwloc5 libmunge2 libxm4 libjemalloc1 xterm openjdk-8-jre-headless \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# turn off password requirement for sudo groups users
RUN sed -i "s/^\%sudo\tALL=(ALL:ALL)\sALL/%sudo ALL=(ALL) NOPASSWD:ALL/" /etc/sudoers

# Download and install debian packages from Son of Grid Engine
ADD https://arc.liv.ac.uk/downloads/SGE/releases/8.1.9/sge-common_8.1.9_all.deb /root/
ADD https://arc.liv.ac.uk/downloads/SGE/releases/8.1.9/sge-doc_8.1.9_all.deb /root/
ADD https://arc.liv.ac.uk/downloads/SGE/releases/8.1.9/sge_8.1.9_amd64.deb /root/
RUN dpkg -i /root/*.deb

# add files to container from local directory
ADD sge_auto_install.conf /root/sge_auto_install.conf
ADD docker_sge_init.sh /etc/my_init.d/01_docker_sge_init.sh
ADD sge_exec_host.conf /root/sge_hostgrp.conf
ADD sge_exec_host.conf /root/sge_exec_host.conf
ADD sge_queue.conf /root/sge_queue.conf
RUN chmod ug+x /etc/my_init.d/01_docker_sge_init.sh

# setup SGE env
ARG SGE_ROOT=/opt/sge
ARG SGE_CELL=default
RUN ln -s $SGE_ROOT/$SGE_CELL/common/settings.sh /etc/profile.d/sge_settings.sh

# install SGE
RUN useradd -r -m -U -G sudo -d /home/sgeuser -s /bin/bash -c "Docker SGE user" sgeuser
RUN cd $SGE_ROOT && ./inst_sge -m -x -s -auto $HOME/sge_auto_install.conf \
&& sleep 10 \
&& /etc/init.d/sgemaster.docker-sge restart \
&& /etc/init.d/sgeexecd.docker-sge restart \
&& sed -i "s/HOSTNAME/`hostname`/" $HOME/sge_exec_host.conf \
&& sed -i "s/HOSTNAME/`hostname`/" $HOME/sge_hostgrp.conf \
&& /opt/sge/bin/lx-amd64/qconf -au sgeuser arusers \
&& /opt/sge/bin/lx-amd64/qconf -Me $HOME/sge_exec_host.conf \
&& /opt/sge/bin/lx-amd64/qconf -Aq $HOME/sge_queue.conf

# clean up
RUN rm /root/*.deb

# start my_init on execution and pass bash to runit
ENTRYPOINT ["/sbin/my_init", "--"]
CMD ["/bin/bash", "--login"]
