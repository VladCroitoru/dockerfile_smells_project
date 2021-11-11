FROM centos:7


RUN yum install -y python wget make gcc gcc-c++ autoconf automake which \
     \
    # install ssdb \
    && wget -O /tmp/ssdb.tar.gz --no-check-certificate https://github.com/ideawu/ssdb/archive/master.tar.gz \
    && mkdir -p /usr/src/ssdb && tar -xzf /tmp/ssdb.tar.gz -C /usr/src/ssdb --strip-components=1 \
    && yum install -y libtool \
    && cd /usr/src/ssdb && make && make install \
     \
    # install pip \
    && wget -O /tmp/proxy_pool.tar.gz --no-check-certificate https://github.com/jhao104/proxy_pool/archive/master.tar.gz \
     \
    # install proxy_pool \
    && mkdir -p /usr/src/proxy_pool && tar -xzf /tmp/proxy_pool.tar.gz -C /usr/src/proxy_pool --strip-components=1 \
    && wget -q -O - https://bootstrap.pypa.io/get-pip.py | python \
    && cd /usr/src/proxy_pool && pip install -r requirements.txt \
    && cd /usr/src/proxy_pool && sed 's/port = 8889/port = 8888/' -i.bak Config.ini \
     \
    && yum erase -y wget make gcc gcc-c++ autoconf automake \
    && find /var/log -type f -print0 | xargs -0 rm -rf /tmp/* \
    && yum clean all
    
CMD cd /usr/local/ssdb && ./ssdb-server -d ssdb.conf && cd /usr/src/proxy_pool/Run && python main.py


EXPOSE 5000 8888
