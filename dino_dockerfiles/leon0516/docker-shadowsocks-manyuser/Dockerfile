FROM centos:6.7
MAINTAINER from www.dwhd.org by lookback (mondeolove@gmail.com)
RUN yum clean all && \
yum update -y && \
rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-* && \
yum install -y m2crypto python-setuptools git curl iptables-devel && \
easy_install pip && pip install cymysql
RUN git clone -b manyuser https://github.com/breakwa11/shadowsocks.git
#RUN git clone -b manyuser https://github.com/mengskysama/shadowsocks.git
ADD run.sh /run.sh
RUN chmod +x /run.sh
EXPOSE 50000-60000
ENTRYPOINT ["/run.sh"]
CMD ["server.py"]
