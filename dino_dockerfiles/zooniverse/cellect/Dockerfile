FROM zooniverse/ruby:2.3

ENV DEBIAN_FRONTEND noninteractive
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

# Apt-get install dependencies
RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get install -y  autoconf automake libboost-all-dev libffi-dev \
        supervisor git-core && \
    apt-get clean

# Install Cellect
WORKDIR /cellect

ADD . /cellect
RUN bundle install --without development

EXPOSE 80

ADD script/start_puma /opt/start_puma
ADD config/supervisor.conf /etc/supervisor/conf.d/cellect.conf

ENTRYPOINT /usr/bin/supervisord
