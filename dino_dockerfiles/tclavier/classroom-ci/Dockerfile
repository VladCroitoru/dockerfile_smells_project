from debian 
env DEBIAN_FRONTEND noninteractive
run sed -e 's/httpredir.debian.org/debian.mirrors.ovh.net/g' -i /etc/apt/sources.list
arg http_proxy
run apt-get update \
    && apt-get install -y \
      cron \
      git \
      maven2 \
      openjdk-7-jdk \
      openjdk-7-jre-lib \
      ruby \ 
      sudo \
      unicorn \
      wget \
    && apt-get clean
run update-alternatives --set java /usr/lib/jvm/java-7-openjdk-amd64/jre/bin/java
add Gemfile /opt/classroom/
add Gemfile.lock /opt/classroom/
run apt-get update && \
    apt-get install -y ruby bundler sudo libsqlite3-dev && \
    cd /opt/classroom && bundle install --without development test && \
    apt-get remove --purge -y libsqlite3-dev && \
    apt-get autoremove -y &&\
    apt-get clean
add . /opt/classroom/
expose 8080
workdir /opt/classroom
add crontab /etc/cron.d/classroom
cmd ["/opt/classroom/start"]
