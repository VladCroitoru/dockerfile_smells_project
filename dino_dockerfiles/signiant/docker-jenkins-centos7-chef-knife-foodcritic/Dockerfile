FROM centos:centos7
MAINTAINER devops@signiant.com

# Install wget which we need later
RUN yum install -y wget

# Install device mapper libraries for docker
RUN yum install -y device-mapper device-mapper-event device-mapper-libs device-mapper-event-libs

# Install EPEL
RUN rpm -ivh https://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-5.noarch.rpm

# Install the repoforge repo (needed for updated git)
RUN wget http://pkgs.repoforge.org/rpmforge-release/rpmforge-release-0.5.3-1.el7.rf.x86_64.rpm -O /tmp/repoforge.rpm
RUN yum install -y /tmp/repoforge.rpm
RUN rm -f /tmp/repoforge.rpm

# Install yum packages
COPY yum-packages.list /tmp/yum.packages.list
RUN chmod +r /tmp/yum.packages.list
RUN yum install -y -q `cat /tmp/yum.packages.list`

# Install PIP - useful everywhere
RUN /usr/bin/curl -O https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py

# make sure we're running latest of everything
RUN yum update -y

# Add our bldmgr user
ENV BUILD_USER bldmgr
ENV BUILD_PASS bldmgr
ENV BUILD_USER_ID 10012
ENV BUILD_USER_GROUP users
ENV BUILD_DOCKER_GROUP docker
ENV BUILD_DOCKER_GROUP_ID 1001

# Create the docker group
RUN groupadd -g $BUILD_DOCKER_GROUP_ID $BUILD_DOCKER_GROUP

RUN adduser -u $BUILD_USER_ID -g $BUILD_USER_GROUP $BUILD_USER
#RUN passwd -f -u $BUILD_USER
RUN echo $BUILD_USER:$BUILD_PASS |chpasswd

# Add the user to the docker group
RUN usermod -a -G $BUILD_DOCKER_GROUP $BUILD_USER

# Install Java
ENV JAVA_VERSION 7u79
ENV BUILD_VERSION b15
ENV JAVA_HOME /usr/java/latest

# Downloading Oracle Java
RUN wget --no-cookies --no-check-certificate --header "Cookie: oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-pub/java/jdk/$JAVA_VERSION-$BUILD_VERSION/jdk-$JAVA_VERSION-linux-x64.rpm" -O /tmp/jdk-7-linux-x64.rpm
RUN yum -y install /tmp/jdk-7-linux-x64.rpm
RUN rm -f /tmp/jdk-7-linux-x64.rpm

RUN alternatives --install /usr/bin/java jar /usr/java/latest/bin/java 200000
RUN alternatives --install /usr/bin/javaws javaws /usr/java/latest/bin/javaws 20000
RUN alternatives --install /usr/bin/javac javac /usr/java/latest/bin/javac 200000

# Create the folder we use for Jenkins workspaces across all nodes
RUN mkdir -p /var/lib/jenkins
RUN chown -R $BUILD_USER:$BUILD_USER_GROUP /var/lib/jenkins

# Make our build user require no tty
RUN echo "Defaults:$BUILD_USER !requiretty" >> /etc/sudoers

# Add user to sudoers with NOPASSWD
RUN echo "$BUILD_USER ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Install and configure SSHD (needed by the Jenkins slave-on-demand plugin)
RUN ssh-keygen -q -N "" -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key
RUN ssh-keygen -q -N "" -t ed25519 -f /etc/ssh/ssh_host_ed25519_key
RUN ssh-keygen -q -N "" -t rsa -f /etc/ssh/ssh_host_rsa_key
RUN sed -ri 's/session    required     pam_loginuid.so/#session    required     pam_loginuid.so/g' /etc/pam.d/sshd
RUN sed -ri 's/#PermitEmptyPasswords no/PermitEmptyPasswords yes/g' /etc/ssh/sshd_config
RUN mkdir -p /home/$BUILD_USER/.ssh
RUN chown -R $BUILD_USER:$BUILD_USER_GROUP /home/$BUILD_USER
RUN chmod 700 /home/$BUILD_USER/.ssh
# Set the timezone
#RUN sed -ri '/ZONE=/c ZONE="America\/New York"' /etc/sysconfig/clock
#RUN rm -f /etc/localtime && ln -s /usr/share/zoneinfo/America/New_York /etc/localtime



#install RVM 2.1.2

RUN /bin/bash -l -c "gpg2 --keyserver hkp://keys.gnupg.net --recv-keys D39DC0E3"
RUN /bin/bash -l -c "curl -L get.rvm.io | bash -s stable"

RUN /bin/bash -l -c "rvm install 2.1.2"

COPY gem.packages.list /tmp/gem.packages.list
RUN chmod +r /tmp/gem.packages.list

RUN /bin/bash -l -c "gem install `cat /tmp/gem.packages.list | tr \"\\n\" \" \"`"

# Folder for secure files
RUN mkdir /etc/chef

RUN ln -s /etc/chef ~/.chef

# Make sure anything/everything we put in the build user's home dir is owned correctly
RUN chown -R $BUILD_USER:$BUILD_USER_GROUP /home/$BUILD_USER  

EXPOSE 22

# This entry will either run this container as a jenkins slave or just start SSHD
# If we're using the slave-on-demand, we start with SSH (the default)

# Default Jenkins Slave Name
ENV SLAVE_ID JAVA_NODE
ENV SLAVE_OS Linux

ADD start.sh /
RUN chmod 777 /start.sh

CMD ["sh", "/start.sh"]
