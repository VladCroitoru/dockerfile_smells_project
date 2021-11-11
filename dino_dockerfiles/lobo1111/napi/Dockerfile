from centos:6

RUN yum install -y wget git samba-client cifs-utils
RUN wget http://packages.sw.be/rpmforge-release/rpmforge-release-0.5.2-2.el6.rf.i686.rpm
RUN rpm -ivh rpmforge-release-0.5.2-2.el6.rf.i686.rpm
RUN yum -y install p7zip
RUN cd /opt; git clone https://github.com/dagon666/napi.git
RUN cd /opt/napi; ./install.sh

ENV SMB_ENABLE true
ENV SMB_PATH URL
ENV SMB_USER smb_user
ENV SMB_PWD smb_pwd

ENV SLEEP 300

COPY start.sh /opt/
RUN chmod +x /opt/start.sh

VOLUME /mnt/storage

WORKDIR /opt/
ENTRYPOINT ./start.sh