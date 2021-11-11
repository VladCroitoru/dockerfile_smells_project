FROM ubuntu

RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get install -y language-pack-en
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

RUN locale-gen en_US.UTF-8
RUN dpkg-reconfigure locales

ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get install -y ruby
RUN \
  /bin/bash -l -c 'gem install flickraw-cached micro-optparse exifr'

RUN mkdir -p /root/photobot/
RUN mkdir -p /data/photos
ADD ./sync.rb /root/photobot/
ADD ./login.rb /root/photobot/
ADD ./start-sync.sh /root/photobot/

VOLUME /data/photos

CMD ["/root/photobot/start-sync.sh"]
