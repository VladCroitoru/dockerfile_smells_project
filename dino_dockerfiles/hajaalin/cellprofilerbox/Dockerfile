FROM hajaalin/cellprofiler

RUN yum install -y \
openssh-server \
xauth \
augeas \
git \
unzip \
java-1.7.0-openjdk-devel \
&& mkdir /var/run/sshd

RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key

ENV SSHD_CONFIG /files/etc/ssh/sshd_config
RUN augtool set ${SSHD_CONFIG}/UsePAM no \
&& augtool set ${SSHD_CONFIG}/X11Forwarding yes \
&& augtool set ${SSHD_CONFIG}/X11UseLocalhost no \
&& augtool set ${SSHD_CONFIG}/KerberosAuthentication no \
&& augtool set ${SSHD_CONFIG}/GSSAPIAuthentication no

# Create user. Set same UID as in data container...
RUN useradd -s /bin/bash -u 1000 dev \
&& chown -R dev: /home/dev \
&& echo 'dev:123'|chpasswd

# Create a shared data volume
# We need to create an empty file, otherwise the volume will
# belong to root.
# This is probably a Docker bug.
RUN mkdir /var/shared/ \
&& touch /var/shared/placeholder \
&& chown -R dev:dev /var/shared
VOLUME /var/shared

WORKDIR /home/dev
ENV HOME /home/dev

# Link in shared parts of the home directory
RUN ln -s /var/shared/.ssh
RUN ln -s /var/shared/.bash_history
RUN ln -s /var/shared/.gitconfig

# Add a script for downloading ImageJ plugins
ADD getImageJPlugins.sh /home/dev/
ADD plugins.config.LoG3D /home/dev/
RUN mkdir plugins

RUN chown -R dev: /home/dev

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"] 
