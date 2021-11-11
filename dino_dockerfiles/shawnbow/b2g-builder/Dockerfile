FROM ubuntu:14.04
MAINTAINER Shawn Bow <shawnbow81@gmail.com>

RUN dpkg --add-architecture i386
# The first apt-get install is for deps listed at
# https://developer.mozilla.org/zh-TW/Firefox_OS/Firefox_OS_build_prerequisites#Ubuntu_13.10
# The second are deps that are needed but not in the minimal ubuntu 14.04 base image.
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends autoconf2.13 bison bzip2 ccache curl flex gawk gcc g++ g++-multilib gcc-4.7 g++-4.7 g++-4.7-multilib git lib32ncurses5-dev lib32z1-dev libgconf2-dev zlib1g:amd64 zlib1g-dev:amd64 zlib1g:i386 zlib1g-dev:i386 libgl1-mesa-dev libx11-dev make zip libxml2-utils lzop && \
    apt-get install -y python python-dev openjdk-7-jdk wget libdbus-glib-1-dev libxt-dev unzip tree patch vim screen openssh-server subversion

# Install latest nodejs
RUN mkdir /nodejs && curl https://nodejs.org/dist/v4.2.0/node-v4.2.0-linux-x64.tar.gz | tar xvzf - -C /nodejs --strip-components=1 && \
    echo "export PATH=/nodejs/bin:\$PATH:" >> /etc/bash.bashrc && /nodejs/bin/npm install -g bower

# We need to use gcc-4.7 to build, set that as default.
RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.7 1
RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.8 2
RUN update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-4.7 1
RUN update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-4.8 2
RUN update-alternatives --set gcc "/usr/bin/gcc-4.7"
RUN update-alternatives --set g++ "/usr/bin/g++-4.7"

# Setup build user
#RUN useradd -m build && echo 'build:build' |chpasswd
#RUN chown -R build:build /home
#ENV SHELL /bin/bash
#ENV HOME /home/build

# Setup sshd
RUN mkdir /var/run/sshd && \
    echo 'root:root' |chpasswd && \
    sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
