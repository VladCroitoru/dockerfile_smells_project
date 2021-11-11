from ubuntu:artful

MAINTAINER alljoynsville

ENV DOWNLOAD_URL http://download.eclipse.org/technology/epp/downloads/release/oxygen/R/eclipse-cpp-oxygen-R-linux-gtk-x86_64.tar.gz
ENV INSTALLATION_DIR /usr/local

RUN DEBIAN_FRONTEND=noninteractive apt-get -yqq update \
 && DEBIAN_FRONTEND=noninteractive apt-get -yqq install openssh-server xorg libgtk2.0-0 default-jre \
    build-essential scons valgrind cmake gcc-multilib ccache quilt libncurses5-dev zlib1g-dev \
    sudo vim curl wget unzip python python-pip gawk flex gettext locales \
    subversion git-core \
 && mkdir /var/run/sshd \
 && useradd -m eclipse -s /bin/bash -u 1001 \
 && echo 'eclipse ALL=NOPASSWD: ALL' > /etc/sudoers.d/eclipse \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN locale-gen en_US.UTF-8
ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8'

RUN echo "X11UseLocalhost no" >> /etc/ssh/sshd_config 
RUN curl -s -L "$DOWNLOAD_URL" | tar xz -C $INSTALLATION_DIR/ \
 && ln -s $INSTALLATION_DIR/eclipse/eclipse /usr/bin/ 

RUN chown -R eclipse:eclipse $INSTALLATION_DIR/eclipse &&\
  chmod -R 775 $INSTALLATION_DIR/eclipse
CMD ["/usr/sbin/sshd", "-D"]
