FROM rdehuyss/docker-ubuntu-java8

MAINTAINER Ronald Dehuysser <ronald.dehuysser@vdab.be>

# patched hornetq-2.4 for VDAB
# Expose hornetq
ADD hornetq-2.4.1.Final /opt/hornetq-2.4.1.Final
ADD hornetq  /etc/init.d/hornetq

RUN chmod a+x /etc/init.d/hornetq
RUN chmod a+x /opt/hornetq-2.4.1.Final/bin/*.sh
RUN echo 'export HORNETQ_HOME=/opt/hornetq-2.4.1.Final' >> /etc/bash.bashrc
RUN echo 'export PATH=$HORNETQ_HOME/bin:$PATH' >> /etc/bash.bashrc

# Expose ports
EXPOSE 1099

CMD service hornetq start; \
	/usr/sbin/sshd -D
