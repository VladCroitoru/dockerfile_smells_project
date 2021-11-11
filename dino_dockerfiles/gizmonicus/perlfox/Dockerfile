FROM centos:6
RUN yum -y clean all && \
    yum -y install \
        firefox \
        java \
        icedtea-web.x86_64 \
        openssh-server \
        xauth \
        xterm && \
    yum -y clean all

ADD ./run.sh /usr/local/bin/run.sh

EXPOSE 22

CMD ["/usr/local/bin/run.sh"]
