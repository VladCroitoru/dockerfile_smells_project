FROM ubuntu:16.04

RUN mkdir /work
WORKDIR /work
ADD Gemfile /work
ADD scraiping.rb /work
ADD lib /work/lib
RUN apt-get -y update && apt-get -y upgrade
RUN apt-get -y install ruby ruby-dev
RUN apt-get -y install zlib1g-dev
RUN gem install bundle
RUN apt-get -y install gcc
RUN apt-get -y install ruby-full
RUN apt-get -y install build-essential patch
RUN bundle install
RUN mkdir /data_mnt
CMD ["bundle", "exec", "ruby", "scraiping.rb"]
