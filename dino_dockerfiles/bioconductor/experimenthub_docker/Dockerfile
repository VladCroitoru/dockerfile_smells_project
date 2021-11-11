# call me bioconductor/experimenthub_docker

FROM ubuntu:18.04

EXPOSE 3000

RUN DEBIAN_FRONTEND=noninteractive \
    apt-get update && apt-get dist-upgrade -y

RUN DEBIAN_FRONTEND=noninteractive \
    apt-get install -y \
    curl g++ git libsqlite3-dev make patch rsync subversion \
    build-essential zlib1g-dev libssl-dev libreadline-dev libyaml-dev \
    libxml2-dev libxslt-dev libffi-dev mysql-client \
    libmysqlclient-dev

RUN git clone https://github.com/rbenv/rbenv.git ~/.rbenv

RUN echo 'eval "$(rbenv init -)"' >> ~/.bash_profile

RUN git clone https://github.com/rbenv/ruby-build.git ~/.rbenv/plugins/ruby-build

RUN ./root/.rbenv/plugins/ruby-build/install.sh

ENV PATH /root/.rbenv/bin:/root/.rbenv/shims:$PATH
ENV CONFIGURE_OPTS --disable-install-doc

#RUN source ~/.bash_profile

RUN rbenv install -v 2.6.5
RUN rbenv global 2.6.5

RUN cd /tmp && curl -LO https://raw.githubusercontent.com/Bioconductor/HubServer/master/Gemfile && \
    gem install bundler && bundle install

# To Run/test locally when updating ruby gems
#ADD Gemfile /tmp/Gemfile
#RUN cd /tmp && gem install bundler && bundle install


ENV HUBSERVER_DATABASE_TYPE mysql

RUN echo hi2

ADD start.sh /tmp/start.sh
ADD start.sql /tmp/start.sql
ADD config.yml /tmp/config.yml
ADD backup_db.sh /bin/backup_db.sh
