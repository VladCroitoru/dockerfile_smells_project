FROM ubuntu:14.04
MAINTAINER Ali Fırat ARI alifiratari@gmail.com
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -y update
RUN apt-get install -y language-pack-en vim wget
RUN update-locale LANG=en_US.UTF-8
RUN dpkg-reconfigure locales

# Add the BigBlueButton key
RUN wget http://ubuntu.bigbluebutton.org/bigbluebutton.asc -O- | apt-key add -

# Add the BigBlueButton repository URL and ensure the multiverse is enabled
RUN echo "deb http://ubuntu.bigbluebutton.org/trusty-1-0/ bigbluebutton-trusty main" | sudo tee /etc/apt/sources.list.d/bigbluebutton.list

#Add multiverse repo
RUN echo "deb http://us.archive.ubuntu.com/ubuntu/ lucid multiverse" | tee -a /etc/apt/sources.list
RUN apt-get -y update
RUN apt-get -y dist-upgrade

#Install LibreOffice
RUN wget http://bigbluebutton.googlecode.com/files/openoffice.org_1.0.4_all.deb
RUN dpkg -i openoffice.org_1.0.4_all.deb
RUN apt-get install -y python-software-properties
RUN apt-get install -y software-properties-common
RUN apt-add-repository ppa:libreoffice/libreoffice-4-4
RUN apt-get -y update
RUN apt-get install -y --allow-unauthenticated libreoffice-common libreoffice

#Install required Ruby version
RUN apt-get install -y libffi-dev
RUN yum install -y git-core zlib zlib-devel gcc-c++ patch readline readline-devel libyaml-devel libffi-devel openssl-devel make bzip2 autoconf automake libtool bison curl sqlite-devel
RUN apt-get install -y curl git-core libffi6 libreadline5 libyaml-0-2 libgdbm3 libcurl4-openssl-dev libxslt1-dev libxml2-dev libssl-dev libreadline-dev libyaml-dev libsqlite3-dev
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3
RUN curl -sSL https://get.rvm.io | bash -s stable --ruby=jruby --gems=rails,puma
RUN echo "source /etc/profile.d/rvm.sh" >> /etc/profile
RUN echo "rvm install 2.3.0 --binary --autolibs=enabled"
RUN echo "rvm install 1.9.3 --binary --autolibs=enabled"
RUN echo "rvm --default use 1.9.3" >> /etc/profile

#Install ffmpeg
RUN apt-get install -y build-essential git-core checkinstall yasm texi2html libvorbis-dev libx11-dev libvpx-dev libxfixes-dev zlib1g-dev pkg-config netcat libncurses5-dev
ADD deb/ffmpeg_5:2.0.1-1_amd64.deb /tmp/
RUN dpkg -i /tmp/ffmpeg_5:2.0.1-1_amd64.deb
RUN rm -f /tmp/*.deb

#Install Tomcat prior to bbb installation
RUN apt-get install -y tomcat7

#Replace init script, installed one is broken
ADD scripts/tomcat7 /etc/init.d/

#Install BigBlueButton
RUN apt-get -y update
RUN gem install bundler
RUN gem install archive-tar-minitar 
RUN gem install hoe -v 2.8.0
RUN gem install rcov -v 0.9.11
RUN su - -c "apt-get install -y bigbluebutton" 

EXPOSE 80 9123 1935

#Add helper script to start bbb
ADD scripts/bbb-start.sh /usr/bin/

CMD ["/usr/bin/bbb-start.sh"]
