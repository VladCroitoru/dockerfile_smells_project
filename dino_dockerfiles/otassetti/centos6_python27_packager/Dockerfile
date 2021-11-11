FROM centos:6
# Centos 6 with python 2.7 from scl and Pyinstaller ready
RUN yum makecache fast && yum install -y centos-release-scl-rh && yum install -y python27 xz && yum clean all 

RUN source /opt/rh/python27/enable && pip2.7 install --upgrade pip && pip2.7 install PyInstaller
RUN curl -L  https://github.com/upx/upx/releases/download/v3.94/upx-3.94-amd64_linux.tar.xz | tar -xJ -C /opt/

ENTRYPOINT ["scl", "enable", "python27", "--", "bash", "-c"]

