# extend the official jenkins slave base image
FROM openshift/jenkins-slave-base-centos7

# specify wanted version of python
ENV PYTHON_VERSION 3.6.1

# install python
RUN set -x \
    && chown -R root:root /home/jenkins \
    && INSTALL_PKGS="gcc make openssl-devel wget zlib-devel" \
    && yum install -y --setopt=tsflags=nodocs $INSTALL_PKGS \
    && cd /tmp \
    && wget https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz \
    && tar xzf Python-${PYTHON_VERSION}.tgz \
    && cd Python-${PYTHON_VERSION} \
    && ./configure \
    && make altinstall \
    && cd .. \
    && rm -rf Python-${Python_VERSION} \
    && yum remove -y $INSTALL_PKGS \
    && yum clean all \
    && chown 1001:0 /home/jenkins

# switch to non-root for openshift usage
USER 1001

# TODO: setup virtualenv?
# RUN set -x \
#    && pip install virtualenv
