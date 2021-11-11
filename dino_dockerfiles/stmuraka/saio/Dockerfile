# OpenStack Swift All-In-One image for testing
# http://docs.openstack.org/developer/swift/development_saio.html
# This image uses a loopback file as the swift block device

FROM ubuntu:xenial
MAINTAINER Shaun Murakami (stmuraka@us.ibm.com)
ENV SWIFT_USER="swift"

### Install required packages ###
RUN apt-get update --fix-missing \
 &&  apt-get install -y \
        sudo \
        rsyslog \
        software-properties-common \
        python-software-properties \
        build-essential \
        autoconf \
        automake \
        libtool \
        curl gcc memcached rsync sqlite3 xfsprogs \
        git-core libffi-dev python-setuptools \
        libssl-dev \
        python-coverage python-dev python-nose \
        python-xattr python-eventlet \
        python-greenlet python-pastedeploy \
        python-netifaces python-pip python-dnspython \
        python-mock

# Build and install liberasurecode
ARG liberasurecode_release=1.4.0
WORKDIR /opt
RUN git clone https://github.com/openstack/liberasurecode.git
ENV LIBERASURECODE_DIR="/opt/liberasurecode"
WORKDIR ${LIBERASURECODE_DIR}
RUN git checkout ${liberasurecode_release} \
 && ./autogen.sh \
 && ./configure \
 && make \
 && make test \
 && make install \
 && ldconfig

### update pip and other supporting packages ###
RUN pip install pip setuptools ndg-httpsclient --upgrade

# Create swift user account
RUN useradd -m -d /home/${SWIFT_USER} -s /bin/bash ${SWIFT_USER} \
 && adduser ${SWIFT_USER} sudo \
 && adduser ${SWIFT_USER} adm \
 && echo "${SWIFT_USER} ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

### Setup for loopback device ###
# Create mount path for loopback disk
RUN mkdir -p /srv
VOLUME /srv

# Common Post-Device Setup
RUN mv /etc/rc.local /etc/rc.local.orig
COPY rc.local /etc/rc.local

### Get the python-swiftclient code ###
USER ${SWIFT_USER}
ENV USER=${SWIFT_USER}
WORKDIR /home/${SWIFT_USER}
# 1. Check out the python-swiftclient repo:
ARG swiftclient_release=3.3.0
RUN git clone https://github.com/openstack/python-swiftclient.git

# 2. Build a development installation of python-swiftclient:
RUN  cd ${HOME}/python-swiftclient \
 && git checkout ${swiftclient_release} \
 && sudo python setup.py develop \
 && cd -

# 3. Check out the swift repo:
ARG swift_release=2.13.0
RUN git clone https://github.com/openstack/swift.git

# 4. Build a development installation of swift:
RUN cd ${HOME}/swift \
 && git checkout ${swift_release} \
 && sudo -H pip install -r requirements.txt \
 && sudo python setup.py develop \
 && cd -

# 5. Install swift's test dependencies:
RUN cd ${HOME}/swift \
 && sudo -H pip install -r test-requirements.txt

### Setting up rsync ###
RUN sudo cp ${HOME}/swift/doc/saio/rsyncd.conf /etc/ \
 && sudo sed -i -e "s/<your-user-name>/${SWIFT_USER}/" /etc/rsyncd.conf \
 && sudo sed -i -e "/^RSYNC_ENABLE.*/ s/^/#/" /etc/default/rsync \
 && sudo sed -i -e "/^#RSYNC_ENABLE.*/a RSYNC_ENABLE=true" /etc/default/rsync

### Setting up rsyslog for individual logging ###
RUN sudo mkdir -p /etc/rsyslog.d \
 && sudo cp ${HOME}/swift/doc/saio/rsyslog.d/10-swift.conf /etc/rsyslog.d/ \
 && sudo sed -i -e "s/\$PrivDropToGroup.*/\$PrivDropToGroup adm/" /etc/rsyslog.conf \
 && sudo mkdir -p /var/log/swift \
 && sudo chown -R syslog.adm /var/log/swift \
 && sudo chmod -R g+w /var/log/swift

### Configure Swift node ###
RUN sudo rm -rf /etc/swift \
 && cd ${HOME}/swift/doc \
 && sudo cp -r saio/swift /etc/swift \
 && cd - \
 && sudo chown -R ${SWIFT_USER}:${SWIFT_USER} /etc/swift \
 && find /etc/swift/ -name \*.conf | xargs sudo sed -i "s/<your-user-name>/${SWIFT_USER}/" \
 && grep changeme /etc/swift/*.conf | cut -d ':' -f1 | uniq | xargs sudo sed -i "s/changeme/$(openssl rand -hex 16)/" \
 && sed -i -e 's/^bind_ip =.*$/bind_ip = 0.0.0.0/' /etc/swift/proxy-server.conf

###  Setting up scripts for running Swift ###
RUN mkdir -p ${HOME}/bin \
 && cd ${HOME}/swift/doc \
 && cp saio/bin/* ${HOME}/bin \
 && cd - \
 && chmod +x ${HOME}/bin/*

# FIX resetswift script (as of 28Feb2017)
RUN sed -i -e '/^find \/var\/cache\/swift/,$d' ${HOME}/bin/resetswift \
 && echo 'if [ $(sudo find /var/cache -type d -name "swift*" 2>/dev/null | wc -l ) != "0" ] ; then' >> ${HOME}/bin/resetswift \
 && echo '    sudo find /var/cache/swift* -type f -name *.recon -exec rm -f {} \;' >> ${HOME}/bin/resetswift \
 && echo 'fi' >> ${HOME}/bin/resetswift \
 && echo 'sudo /etc/init.d/rsyslog restart' >> ${HOME}/bin/resetswift \
 && echo 'sudo /etc/init.d/memcached restart' >> ${HOME}/bin/resetswift

# Create startall script
RUN cp ${HOME}/bin/startmain ${HOME}/bin/startall \
 && sed -i -e 's/main/all/' ${HOME}/bin/startall

# Install the sample configuration file for running tests:
COPY test.conf /etc/swift/test.conf
ENV SWIFT_TEST_CONFIG_FILE="/etc/swift/test.conf" \
    PATH="/home/${SWIFT_USER}/bin:${PATH}"
RUN echo "export PATH=${HOME}/bin:${PATH}" >> ${HOME}/.bashrc \
 && . ${HOME}/.bashrc
# Copy swift test script
COPY runTests.sh /home/${SWIFT_USER}


# Specify loopback device
ENV SAIO_BLOCK_DEVICE="/srv/swift-disk"

# Copy start script
COPY start.sh /home/${SWIFT_USER}

# Copy liberasurecode check script
COPY liberasurecodeCheck.sh /home/${SWIFT_USER}

# Fix ownership
RUN sudo chown ${SWIFT_USER}.${SWIFT_USER} /etc/swift/proxy-server.conf \
 && sudo chown ${SWIFT_USER}.${SWIFT_USER} /home/${SWIFT_USER}/*.sh

# Expose Swift proxy port
EXPOSE 8080

# Run start script
CMD ./start.sh
