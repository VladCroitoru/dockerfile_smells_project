FROM debian:wheezy
MAINTAINER devops@signiant.com

ENV BUILD_USER bldmgr
ENV BUILD_USER_GROUP users

# Set the timezone
RUN rm -f /etc/localtime && ln -s /usr/share/zoneinfo/America/New_York /etc/localtime

# Set the default locale
COPY locale /etc/default/locale
RUN chmod a+r /etc/default/locale

# Update everything installed
RUN apt-get -y update
RUN apt-get -y upgrade

# Install a base set of packages from the default repo
COPY apt-packages.list /tmp/apt-packages.list
RUN chmod +r /tmp/apt-packages.list
RUN apt-get install -y `cat /tmp/apt-packages.list`

# Install PIP - useful everywhere

RUN /usr/bin/curl -O https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py

# Add our bldmgr user
ENV BUILD_USER bldmgr
ENV BUILD_PASS bldmgr
ENV BUILD_USER_ID 10012
ENV BUILD_USER_GROUP users
ENV BUILD_DOCKER_GROUP docker
ENV BUILD_DOCKER_GROUP_ID 1001

# Create the docker group
RUN groupadd --gid $BUILD_DOCKER_GROUP_ID $BUILD_DOCKER_GROUP

RUN useradd -u $BUILD_USER_ID -G $BUILD_USER_GROUP $BUILD_USER
#RUN passwd -f -u $BUILD_USER
RUN echo $BUILD_USER:$BUILD_PASS |chpasswd

# Add the user to the docker group
RUN usermod -a -G $BUILD_DOCKER_GROUP $BUILD_USER

# Create the folder we use for Jenkins workspaces across all nodes
RUN mkdir -p /var/lib/jenkins
RUN chown -R $BUILD_USER:$BUILD_USER_GROUP /var/lib/jenkins

# Add in our common jenkins node tools for bldmgr
COPY jenkins_nodes /home/$BUILD_USER/jenkins_nodes

# Make our build user require no tty
RUN echo "Defaults:$BUILD_USER !requiretty" >> /etc/sudoers

# Add user to sudoers with NOPASSWD
RUN echo "$BUILD_USER ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Install Java
RUN apt-get -y install openjdk-7-jdk

# Install ant
ENV ANT_VERSION 1.9.6
RUN cd && \
    wget -q http://archive.apache.org/dist/ant/binaries/apache-ant-${ANT_VERSION}-bin.tar.gz && \
    tar -xzf apache-ant-${ANT_VERSION}-bin.tar.gz && \
    mv apache-ant-${ANT_VERSION} /usr/local/apache-ant-${ANT_VERSION} && \
    rm apache-ant-${ANT_VERSION}-bin.tar.gz
RUN sh -c 'echo ANT_HOME=/usr/local/apache-ant-${ANT_VERSION} >> /etc/environment'
ENV ANT_HOME /usr/local/apache-ant-${ANT_VERSION}

# Install our required ant libs
COPY ant-libs/*.jar ${ANT_HOME}/lib/
RUN chmod 644 ${ANT_HOME}/lib/*.jar

# Install link to ant
RUN update-alternatives --install /usr/bin/ant ant ${ANT_HOME}/bin/ant 20000

# Install and configure SSHD (needed by the Jenkins slave-on-demand plugin)
RUN ssh-keygen -y -q -N "" -t dsa -f /etc/ssh/ssh_host_dsa_key
RUN ssh-keygen -y -q -N "" -t rsa -f /etc/ssh/ssh_host_rsa_key
RUN sed -ri 's/session    required     pam_loginuid.so/#session    required     pam_loginuid.so/g' /etc/pam.d/sshd
RUN sed -ri 's/#PermitEmptyPasswords no/PermitEmptyPasswords yes/g' /etc/ssh/sshd_config
RUN mkdir -p /home/$BUILD_USER/.ssh
RUN chown -R $BUILD_USER:$BUILD_USER_GROUP /home/$BUILD_USER
RUN chmod 700 /home/$BUILD_USER/.ssh
RUN mkdir /var/run/sshd

# Add in our build specific paths
RUN mkdir -p /opt/corp/local/ant/bin
RUN ln -s /usr/bin/ant /opt/corp/local/ant/bin/ant
RUN chown -R $BUILD_USER:$BUILD_USER_GROUP /opt/corp

EXPOSE 22

# This entry will either run this container as a jenkins slave or just start SSHD
# If we're using the slave-on-demand, we start with SSH (the default)

# Default Jenkins Slave Name
ENV SLAVE_ID JAVA_NODE
ENV SLAVE_OS Linux

ADD start.sh /
RUN chmod 777 /start.sh

CMD ["sh", "/start.sh"]
