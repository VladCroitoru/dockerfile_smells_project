FROM centos:7

MAINTAINER Wang Lilong "wanglilong007@gmail.com"

ENV VERSION=6.1.0
ENV MYSQL_VERSION=5.7.20
ENV MYSQL_DOWNLOAD_URL=https://downloads.mysql.com/archives/get/file/mysql-$MYSQL_VERSION-1.el7.x86_64.rpm-bundle.tar

RUN set -x \  
	&& yum install -y epel-release \
	&& yum install -y python-pip tftp-server syslinux-tftpboot xinetd dhcp ipmitool \
	&& buildDeps='curl gcc g++ make python-devel libffi-dev' \
	&& yum install -y $buildDeps iptables-services sudo psmisc \
    && curl -fSL https://github.com/openstack/ironic-inspector/archive/${VERSION}.tar.gz -o ironic-inspector-${VERSION}.tar.gz \
    && tar xf ironic-inspector-${VERSION}.tar.gz \
    && cd ironic-inspector-${VERSION} \
    && sed -i 's/>/=/g' requirements.txt \
    && pip install -r requirements.txt \
    && PBR_VERSION=${VERSION}  pip install . \
    && mkdir /etc/ironic-inspector \
    && cp rootwrap.conf /etc/ironic-inspector \
    && cp rootwrap.d /etc/ironic-inspector -rf \
    && cp ironic_inspector/migrations/ /usr/lib/python2.7/site-packages/ironic_inspector/ -rf \
    && cp ironic_inspector/alembic.ini /usr/lib/python2.7/site-packages/ironic_inspector/ -rf \
    && pip install PyMySQL pymemcache\
    && cd - \
    && rm -rf ironic-inspector-${VERSION}* \
    && echo "install mysql .............................." \
    && yum install -y numactl net-tools \
    && curl -fSL $MYSQL_DOWNLOAD_URL -o msyql.tar.gz \
    && tar xf msyql.tar.gz \
    && yum install -y mysql-community-common-$MYSQL_VERSION-1.el7.x86_64.rpm  \
    && yum install -y mysql-community-libs-$MYSQL_VERSION-1.el7.x86_64.rpm  \
    && yum install -y mysql-community-client-$MYSQL_VERSION-1.el7.x86_64.rpm  \
    && yum install -y mysql-community-server-$MYSQL_VERSION-1.el7.x86_64.rpm \
    && rm *.rpm msyql.tar.gz -rf \
    && mysqld --initialize \
    && chown mysql:mysql -R /var/lib/mysql* \
    && yum clean all
