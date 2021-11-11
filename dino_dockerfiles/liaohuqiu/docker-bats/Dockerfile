FROM centos
RUN yum install -y bsdtar
RUN curl -fsL https://github.com/sstephenson/bats/archive/master.zip |bsdtar xf - -C /opt/ && \
    cd /opt/bats-master/ && \
    chmod +x ./install.sh && \
    ./install.sh /usr/local && \
    chmod +x /usr/local/libexec/* && \
    ln -sf /usr/local/libexec/bats /usr/local/bin/ && \
    rm -rf /opt/bats-master/
