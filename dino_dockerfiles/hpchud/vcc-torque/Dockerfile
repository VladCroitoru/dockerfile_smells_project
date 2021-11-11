FROM hpchud/vcc-base-centos:7

# install packages required
RUN yum -y install make libtool openssl-devel libxml2-devel boost-devel gcc gcc-c++ git nano openssh-server openssh-clients gcc-gfortran

# build and install torque 5 in one step
WORKDIR /
RUN git clone https://github.com/adaptivecomputing/torque.git -b 5.1.1.2 torque-src \
	&& cd torque-src \
	&& ./autogen.sh \
	&& ./configure --prefix=/usr --disable-posixmemlock --disable-cpuset \
	&& make \
	&& make install \
	&& ldconfig \
	&& cd .. \
	&& cp torque-src/torque.setup . \
	&& rm -r torque-src

# torque config
# we don't have interaction so need to fix setup script
RUN sed -i 's/-t create/-t create -f/' torque.setup \
	&& ./torque.setup root localhost \
	&& qmgr -c "set server auto_node_np=true" \
	&& rm torque.setup

# build and install pdsh
RUN cd /tmp \
	&& git clone https://github.com/grondo/pdsh.git pdsh-build \
	&& cd pdsh-build \
	&& git checkout -q e1c8e71dd6a26b40cd067a8322bd14e10e4f7ded \
	&& ./configure --with-ssh --without-rsh --prefix=/usr --with-machines=/etc/vcc/pdsh_machines \
	&& make \
	&& make install \
	&& cd / \
	&& rm -rf /tmp/pdsh-build

# build and install MAUI
RUN cd /tmp \
	&& git clone https://github.com/jbarber/maui.git maui-build \
	&& cd maui-build \
	&& git checkout -q 7a8513a1317afd57afab6f800d0c15f124d6083f \
	&& ./configure --with-pbs \
	&& make \
	&& make install \
	&& cd / \
	&& rm -rf /tmp/maui-build
COPY maui-config.sh /etc/vcc/maui-config.sh

# build and install mpich
RUN cd /tmp \
	&& curl -O https://www.mirrorservice.org/sites/distfiles.macports.org/mpich/mpich-3.2.tar.gz \
	&& tar xf mpich-*.tar.gz \
	&& cd mpich-* \
	&& ./configure \
	&& make \
	&& make install \
	&& cd / \
	&& rm -rf /tmp/mpich-*

# make links for maui tools
RUN ln -s /usr/local/maui/bin/showq /usr/bin/showq
RUN ln -s /usr/local/maui/bin/showbf /usr/bin/showbf
RUN ln -s /usr/local/maui/bin/showres /usr/bin/showres
RUN ln -s /usr/local/maui/bin/checkjob /usr/bin/checkjob

# install vcc configuration files
COPY init.yml /etc/init.yml
COPY services.yml /etc/services.yml
COPY services-headnode.yml /etc/vcc/services-headnode.yml
COPY services-workernode.yml /etc/vcc/services-workernode.yml
COPY dependencies.yml /etc/vcc/dependencies.yml

# cluster hook scripts
ADD hooks/pbsnodes.sh /etc/vcc/cluster-hooks.d/pbsnodes.sh
ADD hooks/pdsh.sh /etc/vcc/cluster-hooks.d/pdsh.sh
RUN chmod +x /etc/vcc/cluster-hooks.d/*

# service hook scripts
ADD hooks/headnode.sh /etc/vcc/service-hooks.d/headnode.sh
RUN chmod +x /etc/vcc/service-hooks.d/*

# set up SSH config
ADD sshd_config /etc/ssh/sshd_config
RUN echo -e "\tPort 2222" >> /etc/ssh/ssh_config
RUN echo -e "\tStrictHostKeyChecking no" >> /etc/ssh/ssh_config
RUN echo -e "\tUserKnownHostsFile /dev/null" >> /etc/ssh/ssh_config

# add the batchuser user
RUN useradd --create-home --uid 900 --shell /bin/bash batchuser
RUN echo batchuser:batchuser | chpasswd

# add the SSH key for batchuser

RUN mkdir -p /home/batchuser/.ssh
ADD batchuser.id_rsa /home/batchuser/.ssh/id_rsa
ADD batchuser.id_rsa.pub /home/batchuser/.ssh/id_rsa.pub
RUN cat /home/batchuser/.ssh/id_rsa.pub > /home/batchuser/.ssh/authorized_keys
RUN cat /home/batchuser/.ssh/id_rsa.pub > /home/batchuser/.ssh/authorized_keys2

# add example MPI job

ADD hello.job /home/batchuser/hello.job

# fix permissions for batchuser

RUN chmod 700 /home/batchuser/.ssh
RUN chmod 600 /home/batchuser/.ssh/*
RUN chown -R batchuser:batchuser /home/batchuser/.ssh

# set up sshfs
RUN yum -y makecache fast
RUN yum -y install epel-release
RUN yum -y install sshfs

# add the SSH key for root

RUN mkdir -p /root/.ssh
ADD root.id_rsa /root/.ssh/id_rsa
ADD root.id_rsa.pub /root/.ssh/id_rsa.pub
RUN cat /root/.ssh/id_rsa.pub > /root/.ssh/authorized_keys
RUN cat /root/.ssh/id_rsa.pub > /root/.ssh/authorized_keys2
RUN chmod 700 /root/.ssh
RUN chmod 600 /root/.ssh/*

# set up /cluster shared folder
RUN mkdir /cluster
ADD test.sh /root/test.sh