FROM ruby:2.1.5
MAINTAINER mookjp<mookjpy@gmail.com>

VOLUME /data/rubygems
EXPOSE 9292

RUN apt-get update && apt-get install -y nginx

# As old version of gem has problem to call mirror command,
# updating is required.
# https://github.com/rubygems/rubygems-mirror/issues/20
RUN gem update --system && \
    gem install rubygems-mirror geminabox
ADD .mirrorrc /root/.gem/.mirrorrc
ADD config.ru /root/.gem/mirror/config.ru
WORKDIR /root/.gem/mirror

CMD ["rackup", "--host", "0.0.0.0"]
