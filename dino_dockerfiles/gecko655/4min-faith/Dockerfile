FROM ruby
MAINTAINER gecko655 <aqwsedrft1234@yahoo.co.jp>

WORKDIR /root/4min-faith
RUN apt-get update \
    && apt-get -y upgrade \
    && apt-get -y dist-upgrade \
    && apt-get -y autoremove \
    && apt-get -y install rsyslog \
    && apt-get -y install vim \
    && apt-get -y install cmake\
    && apt-get -y install g++\
    && apt-get -y install ocl-icd-libopencl1 \
    && apt-get -y install libopencv-dev
RUN ln /dev/null /dev/raw1394 #for suppress error

RUN touch /tmp/cronlog.log

COPY cascade cascade

COPY secretenv secretenv
RUN (crontab -l; cat secretenv) | crontab
RUN rm secretenv

COPY Gemfile Gemfile
RUN bundle install
COPY test test
COPY Rakefile Rakefile

COPY crontab.config crontab.config
RUN (crontab -l; cat crontab.config ) | crontab

COPY src src
    
CMD rsyslogd && sh -c 'ln /dev/null /dev/raw1394'; cron && tail -f /var/log/syslog /tmp/cronlog.log
