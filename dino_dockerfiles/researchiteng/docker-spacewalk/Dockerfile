#
# Dockerfile - Spacewalk
#
# - Build
# git clone https://github.com/ruo91/docker-spacewalk /opt/docker-spacewalk
# docker build --rm -t spacewalk /opt/docker-spacewalk
#
# - Run
# docker run --privileged=true -d --name="spacewalk" -h "spackewalk" spacewalk

# 1. Base images
FROM     centos:latest
MAINTAINER Yongbok Kim <ruo91@yongbok.net>

# 2. Set the environment variable
WORKDIR /opt

# 3. Add the epel, spacewalk, jpackage repository
ADD conf/jpackage.repo /etc/yum.repos.d/jpackage.repo
RUN rpm -Uvh http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-7.noarch.rpm \
 && rpm -Uvh http://yum.spacewalkproject.org/latest/RHEL/7/x86_64/spacewalk-repo-2.4-3.el7.noarch.rpm

# 4. Installation a spacewalk
ADD conf/answer.txt	/opt/answer.txt
ADD conf/spacewalk.sh	/opt/spacewalk.sh
RUN chmod a+x /opt/spacewalk.sh
RUN yum install -y spacewalk-setup-postgresql spacewalk-postgresql

# 5. Supervisor
RUN yum install -y python-setuptools && easy_install pip && pip install supervisor && pip install 'meld3 == 1.0.1' && mkdir /etc/supervisord.d
ADD conf/supervisord.conf /etc/supervisord.d/supervisord.conf

# 6. Start supervisord
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.d/supervisord.conf"]

# Port
EXPOSE 80 443
