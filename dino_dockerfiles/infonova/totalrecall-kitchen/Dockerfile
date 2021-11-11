FROM centos:centos7

LABEL name="Total Recall CentOS 7 Base Image"

# Dockerfile for systemd based images 
ENV container docker

# https://docs.docker.com/samples/library/centos/#dockerfile-for-systemd-base-image
RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == \
systemd-tmpfiles-setup.service ] || rm -f $i; done); \
# Disabled because of:
# https://forums.fedoraforum.org/showthread.php?311835-sshd-in-docker-In-a-good-boot-who-removes-var-run-nologin
#rm -f /lib/systemd/system/multi-user.target.wants/*;\
rm -f /etc/systemd/system/*.wants/*;\
rm -f /lib/systemd/system/local-fs.target.wants/*; \
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
rm -f /lib/systemd/system/basic.target.wants/*;\
rm -f /lib/systemd/system/anaconda.target.wants/*;

RUN yum -y install epel-release && yum -y install cronie initscripts polkit python-pip python-devel git libselinux-python libffi-devel openssl-devel gcc net-tools && \
    pip install --upgrade pip && pip install setuptools==21.0.0 ansible==2.4.3.0 && \
    curl -s -L https://www.opscode.com/chef/install.sh | bash -s -- -v latest

CMD env GEM_HOME=/tmp/verifier GEM_PATH=/tmp/verifier GEM_CACHE=/tmp/verifier/gems/cache /opt/chef/embedded/bin/gem install thor busser busser-serverspec serverspec bundler && \
    gem install test-kitchen -v 1.8.0 kitchen-docker -v 2.4.0 kitchen-ansible -v 0.45.4 && \
    rm /etc/localtime && ln -s /usr/share/zoneinfo/Europe/Vienna /etc/localtime && localedef -c -i en_US -f UTF-8 en_US.UTF-8 && localedef -c -i de_AT -f UTF--8 de_AT.UTF-8 && \
    systemctl enable crond.service && \
    chown -R kitchen:kitchen /tmp/verifier 

VOLUME [ "/sys/fs/cgroup" ]
CMD ["/usr/sbin/init"]
