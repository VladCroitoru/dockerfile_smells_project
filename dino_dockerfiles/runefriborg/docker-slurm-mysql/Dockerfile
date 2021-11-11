######################################################
#
# Slurm+MySQL - ready to test jobs and configurations
# Centos 6.x based
######################################################

FROM runefriborg/docker-c6-supervisord

MAINTAINER Rune Friborg <runef@birc.au.dk>

# Install dependencies for SLURM and MySQL server
RUN yum -y install openssh-server gcc gcc-g++ make munge munge-devel httpd bzip2 vim-minimal tar perl git mysql-server mysql-devel lua lua-devel

# Configure munge
RUN create-munge-key && \
  chown -R root:root /var/log/munge && \
  chown -R root:root /var/lib/munge && \
  mkdir /var/run/munge && \
  chown -R root:root /var/run/munge && \
  chown -R root:root /etc/munge 

# Install slurm
WORKDIR /usr/local
RUN git clone https://github.com/SchedMD/slurm.git
WORKDIR /usr/local/slurm

# Select SLURM version
RUN git checkout tags/slurm-15-08-4-1

RUN ./configure --prefix=/opt/slurm --sysconfdir=/opt/slurm/etc --silent --with-mysql_config=/usr/bin/ CFLAGS=-Os && \
  make && \
  make install && \
  cd contribs/lua && \
  make install && \
  mkdir -p /var/log/slurm

RUN adduser testuser && \
    echo "testuser:testuser" | chpasswd && \
    echo "export PATH=/opt/slurm/bin:\$PATH" >> /home/testuser/.bashrc

# Copy SLURM configuration files and supervisord files to the container
ADD root /

RUN chown testuser:testuser -R /home/testuser

RUN \
  /etc/init.d/mysqld start && \
  sleep 5 && \
  mysqladmin -u root password 'seCret' && \
  /usr/sbin/munged && \
  /opt/slurm/sbin/slurmdbd && \
  sleep 5 && \
  /opt/slurm/bin/sacctmgr -i add cluster cluster0 && \
  /opt/slurm/bin/sacctmgr -i add account basic cluster=cluster0 Description="The One node cluster" Organization="Big O" && \
  /opt/slurm/bin/sacctmgr -i add user testuser DefaultAccount=basic Account=basic && \
  rm -f var/run/munge/munge.socket.* && \
  /etc/init.d/mysqld stop

EXPOSE 10389 22 6817 6818
