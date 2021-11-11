FROM ruby:2.2.3
MAINTAINER Matthieu ANTOINE <matthieu@matthieu-antoine.me>
ENV BRIMIR_VERSION 0.7.3


RUN mkdir -p /opt/brimir
RUN cd /opt && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 561F9B9CAC40B2F7 && \
    apt-get update && apt-get install -y apt-transport-https ca-certificates python-pip postgresql-client nodejs && \
    git clone https://github.com/ivaldi/brimir /opt/brimir &&  \
    pip install supervisor

WORKDIR /opt/brimir
RUN git checkout tags/$BRIMIR_VERSION
RUN gem install bundler && \
    bundle install --without sqlite mysql development test --deployment

ADD devise.rb config/initializers/devise.rb
COPY docker-entrypoint.sh  /
RUN chmod a+x /docker-entrypoint.sh
ADD loadUser.rb .

EXPOSE 3000


ENTRYPOINT ["/docker-entrypoint.sh"]


# Or "CMD /etc/init.d/postgresql restart && passenger start -a 0.0.0.0 -p 3000 -e production --friendly-error-pages" for debug errors


