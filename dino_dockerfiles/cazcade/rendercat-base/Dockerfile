FROM ubuntu:14.04
MAINTAINER Neil Ellis hello@neilellis.me

# Set working directory.
ENV HOME /root
WORKDIR /root

# Env
ENV SLIMERJS_VERSION_M 0.9
ENV SLIMERJS_VERSION_F 0.9.4
ENV PHANTOM_VERSION 1.9.8

# Update OS.
RUN echo "deb http://archive.ubuntu.com/ubuntu trusty multiverse" >> /etc/apt/sources.list
RUN echo "deb http://archive.ubuntu.com/ubuntu trusty-updates multiverse" >> /etc/apt/sources.list
RUN echo "deb http://archive.ubuntu.com/ubuntu trusty-security multiverse" >> /etc/apt/sources.list
RUN apt-get update

# Required directories
RUN mkdir -p /usr/local
RUN mkdir /data
RUN mkdir /app

#Nasty Downloads
RUN mkdir ~/fonts/
RUN apt-get install -y curl
RUN mkdir -p /usr/share/fonts
RUN curl -L "http://neil-public.s3-website-eu-west-1.amazonaws.com/google-fonts.tgz" | tar -C /usr/share/fonts/ --transform='s/.*\///' -zxvf  -
RUN curl -L "http://neil-public.s3-website-eu-west-1.amazonaws.com/fonts.tgz" | tar -C /usr/share/fonts/ --transform='s/.*\///' -zxvf  -
RUN ls -l /usr/share/fonts
RUN chmod -R 755 /usr/share/fonts


#NodeJS
RUN apt-get install -y wget build-essential software-properties-common
RUN curl -sL https://deb.nodesource.com/setup | sudo bash - && \
    apt-get install -y nodejs && \
    echo '\n# Node.js\nexport PATH="node_modules/.bin:$PATH"' >> /root/.bashrc


# Install basic packages.
RUN apt-get install -y  python-urllib3  perl-base perl libc6  dbus libdbus-glib-1-2  bzip2 git  unzip git-core xvfb timelimit graphicsmagick

# Install Nginx
RUN apt-get install -y nginx

#Fonts
RUN yes |  apt-get install -y msttcorefonts
RUN  apt-get install -y freetype*
RUN  apt-get install -y fonts-cantarell lmodern ttf-aenigma ttf-georgewilliams ttf-bitstream-vera ttf-sjfonts ttf-tuffy tv-fonts
#ubuntustudio-font-meta
RUN fc-cache -fv

#GraphicsMagick
RUN  apt-get install -y graphicsmagick

#CutyCapt
RUN  apt-get install -y cutycapt


# PhantomJS
RUN apt-get install -y libfreetype6 libfontconfig1
RUN apt-get install -y phantomjs

# SlimerJS
RUN apt-get install -y dbus libdbus-glib-1-2  bzip2 firefox
RUN wget -O /tmp/slimerjs-$SLIMERJS_VERSION_F-linux-x86_64.tar.bz2 http://download.slimerjs.org/v$SLIMERJS_VERSION_M/$SLIMERJS_VERSION_F/slimerjs-$SLIMERJS_VERSION_F-linux-x86_64.tar.bz2
RUN tar -xjf /tmp/slimerjs-${SLIMERJS_VERSION_F}-linux-x86_64.tar.bz2 -C /tmp
RUN rm -f /tmp/slimerjs-${SLIMERJS_VERSION_F}-linux-x86_64.tar.bz2
RUN mv /tmp/slimerjs-${SLIMERJS_VERSION_F}/ /usr/local/slimerjs
RUN ln -s /usr/local/slimerjs/slimerjs /usr/local/bin/slimerjs

#Supervisord
RUN apt-get install -y supervisor 



