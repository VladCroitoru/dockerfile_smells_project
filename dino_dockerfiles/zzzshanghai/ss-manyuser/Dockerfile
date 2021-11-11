FROM centos:latest

MAINTAINER zzzshanghai

ENV INSTALL_DIR=/root/shadowsocks

RUN rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-* && \
    yum clean all && \
    yum makecache && \
    yum update -y && \
    yum install -y m2crypto python-setuptools git curl iptables-devel && \
    easy_install pip && pip install shadowsocks cymysql

RUN git clone -b manyuser https://github.com/breakwa11/shadowsocks.git $INSTALL_DIR && \
    cp $INSTALL_DIR/mysql.json $INSTALL_DIR/usermysql.json
    
WORKDIR /root/shadowsocks

RUN chmod +x run.sh server.py setup.py stop.sh

RUN python setup.py install

#EXPOSE 20001

CMD run.sh
