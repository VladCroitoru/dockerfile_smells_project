FROM ubuntu:16.04

# docker build -t ruby-1.9.2-p180_rails-2.3.12:latest .

COPY .emacs .irbrc .tmux.conf /root/

RUN apt-get update
RUN apt-get install -y curl locales-all git subversion man emacs nano tmux fortune-mod fortunes figlet imagemagick ntp tzdata
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 7D2BAF1CF37B13E2069D6956105BD0E739499BDB
# https://github.com/rvm/rvm/issues/4068
RUN curl -sSL https://get.rvm.io | grep -v __rvm_print_headline | bash -s stable --ruby=1.9.2-p180

ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

SHELL ["/bin/bash", "-c"]
RUN echo "source /usr/local/rvm/scripts/rvm" >> /root/.bashrc

RUN source /usr/local/rvm/scripts/rvm; gem update --system 1.6.2 
RUN source /usr/local/rvm/scripts/rvm; gem install rails -v 2.3.12 
RUN source /usr/local/rvm/scripts/rvm; gem install mongrel -v 1.2.0.pre2 
RUN source /usr/local/rvm/scripts/rvm; gem install nokogiri -v 1.6.0 
# ERROR:  Error installing authlogic:
#   i18n requires Ruby version >= 1.9.3.
RUN source /usr/local/rvm/scripts/rvm; gem install authlogic -v 2.1.6; exit 0
RUN source /usr/local/rvm/scripts/rvm; gem install calendar_helper -v 0.2.6 
RUN source /usr/local/rvm/scripts/rvm; gem install cancan -v 1.3.4 
RUN source /usr/local/rvm/scripts/rvm; gem install exchange -v 1.2.2 
RUN source /usr/local/rvm/scripts/rvm; gem install fuzzy_match -v 2.1.0 
RUN source /usr/local/rvm/scripts/rvm; gem install handles_sortable_columns -v 0.1.2 
RUN source /usr/local/rvm/scripts/rvm; gem install hirb -v 0.7.1 
RUN source /usr/local/rvm/scripts/rvm; gem install paperclip -v 2.3.1.1 
RUN source /usr/local/rvm/scripts/rvm; gem install rqrcode -v 0.10.1 
RUN source /usr/local/rvm/scripts/rvm; gem install sqlite3 -v 1.3.8 
RUN source /usr/local/rvm/scripts/rvm; gem install sqlite3-ruby -v 1.3.3 
RUN source /usr/local/rvm/scripts/rvm; gem install will_paginate -v 2.3.15 
RUN source /usr/local/rvm/scripts/rvm; gem install abstract -v 1.0.0 
RUN source /usr/local/rvm/scripts/rvm; gem install algorithms -v 0.6.1 
RUN source /usr/local/rvm/scripts/rvm; gem install atomic -v 1.1.13 
RUN source /usr/local/rvm/scripts/rvm; gem install cheat -v 1.3.3 
RUN source /usr/local/rvm/scripts/rvm; gem install chunky_png -v 1.3.8 
RUN source /usr/local/rvm/scripts/rvm; gem install open4 -v 1.3.4 
RUN source /usr/local/rvm/scripts/rvm; gem install pager -v 1.0.1 
RUN source /usr/local/rvm/scripts/rvm; gem install railroad -v 0.5.0 
RUN source /usr/local/rvm/scripts/rvm; gem install rbtree -v 0.4.1 
RUN source /usr/local/rvm/scripts/rvm; gem install rqrcode -v 0.10.1
RUN source /usr/local/rvm/scripts/rvm; gem install sentient_user -v 0.3.2

# some monkey-patching going on here
COPY timestamp.rb /usr/local/rvm/gems/ruby-1.9.2-p180/gems/activerecord-2.3.12/lib/active_record
COPY sortable_columns.rb /usr/local/rvm/gems/ruby-1.9.2-p180/gems/handles_sortable_columns-0.1.2/lib/handles
COPY processor.rb /usr/local/rvm/gems/ruby-1.9.2-p180/gems/paperclip-2.3.1.1/lib/paperclip

# for fortune
ENV PATH "$PATH:/usr/games"

ENV CONTAINER_TIMEZONE America/Los_Angeles
RUN echo 'echo $CONTAINER_TIMEZONE > /etc/timezone' >> /root/.bashrc
RUN echo 'ln -sf /usr/share/zoneinfo/$CONTAINER_TIMEZONE /etc/localtime' >> /root/.bashrc
RUN echo "dpkg-reconfigure -f noninteractive tzdata" >> /root/.bashrc
