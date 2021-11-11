FROM centos:7.7.1908

##########################################################################
# all yum installations here
RUN yum install -y sudo passwd openssh-server openssh-clients tar screen crontabs strace telnet perl libpcap bc patch ntp dnsmasq unzip pax which less \
                   rng-tools initscripts bind-utils net-tools libselinux-utils \
                   openssl

##########################################################################
# enable services
RUN systemctl enable dnsmasq sshd crond

##########################################################################
# add epel repository
RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm

RUN yum install -y ngrep lsyncd sshpass

# start sshd to generate host keys, patch sshd_config and enable yum repos
RUN (mkdir -p /var/run/sshd; \
     yes|ssh-keygen -f /etc/ssh/ssh_host_rsa_key -t rsa -N ''; \
     yes|ssh-keygen -f /etc/ssh/ssh_host_ecdsa_key -t ecdsa -N ''; \
     yes|ssh-keygen -f /etc/ssh/ssh_host_ed25519_key -t ed25519 -N ''; \
     sed -i 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config; \
     sed -i 's/#UsePAM no/UsePAM no/g' /etc/ssh/sshd_config; \
     sed -i 's/#PermitRootLogin yes/PermitRootLogin yes/' /etc/ssh/sshd_config; \
     sed -i 's/enabled=0/enabled=1/' /etc/yum.repos.d/CentOS-Base.repo)

RUN (mkdir -p /root/.ssh/; \
     rm -f /var/lib/rpm/.rpm.lock; \
     echo "StrictHostKeyChecking=no" > /root/.ssh/config; \
     echo "UserKnownHostsFile=/dev/null" >> /root/.ssh/config)

# --- workaround for agetty high cpu ---
RUN systemctl mask system-getty.slice; \
        systemctl mask getty.target; \
        systemctl mask serial-getty@ttyS0.service; \
        systemctl mask getty@tty1.service

# terminfo for screen.xterm-256color
ADD screen.xterm-256color /root/
RUN tic /root/screen.xterm-256color

##########################################################################
# passwords 
RUN echo "root:password" | chpasswd

EXPOSE 22
CMD ["/sbin/init"]
