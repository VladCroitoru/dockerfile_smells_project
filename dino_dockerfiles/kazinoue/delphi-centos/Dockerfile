FROM centos:7

RUN set -x && \
    yum -y update && \
    yum -y upgrade && \
    yum -y install epel-release wget curl && \
    yum -y install p7zip p7zip-plugins && \
    yum -y install xterm httpd valgrind vim && \
    yum -y groupinstall "Development Tools"

# For 10.2.0
# ADD http://altd.embarcadero.com/releases/studio/19.0/PAServer/LinuxPAServer19.0.tar.gz LinuxPAServer19.0.tar.gz

# For 10.2.3
# ADD http://altd.embarcadero.com/releases/studio/19.0/PAServer/Release3/LinuxPAServer19.0.tar.gz LinuxPAServer19.0.tar.gz

#RUN cd /root && \
#    tar zxvf /LinuxPAServer19.0.tar.gz && \
#    rm /LinuxPAServer19.0.tar.gz
