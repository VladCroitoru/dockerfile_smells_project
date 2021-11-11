FROM centos

MAINTAINER Kenneth D. Evensen <kevensen@redhat.com>

ENV HOME=/opt/app-root/ \
    PATH=/opt/app-root:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH

RUN rpmkeys --import file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7 && \
    yum install -y unzip && \
    yum clean all && \
    rm -rf /var/cache/yum/*


ADD https://s3.amazonaws.com/aws-cli/awscli-bundle.zip /root/
ADD bin/ /usr/bin/

RUN cd /root && \
    unzip awscli-bundle.zip && \
    /root/awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws && \
    aws --version

RUN useradd -u 1001 -r -g 0 -d ${HOME} -s /sbin/nologin -c "Default Application User" default && \
    chown -R 1001:0 /opt/app-root && \
    chmod -R og+rwx /opt/app-root


WORKDIR ${HOME}

USER 1001

CMD ["/usr/bin/run.sh"]
