FROM ruby:2.1.4

RUN mkdir /apps
WORKDIR /apps

#install mysql-server
RUN apt-get update
RUN apt-get -y install mysql-server

#Install some dependencies
RUN git clone https://github.com/vitalsource/LTI2-Reference.git
RUN git clone https://github.com/bsletten/ruby-jsonld-signatures.git

#Cache some gems
COPY Gemfile* /apps/tmp/
WORKDIR /apps/tmp
RUN bundle install --deployment

#Configure mysql-server
RUN /usr/sbin/mysqld & \
    sleep 10s &&\
    echo "GRANT ALL ON *.* TO cbeuser@'%' IDENTIFIED BY 'cbepswd' WITH GRANT OPTION; FLUSH PRIVILEGES" | mysql

ADD ./ /apps/cbe_etranscript_tp

WORKDIR /apps/cbe_etranscript_tp

EXPOSE 4000

CMD ["/bin/bash", "/apps/cbe_etranscript_tp/docker/run.sh"]
