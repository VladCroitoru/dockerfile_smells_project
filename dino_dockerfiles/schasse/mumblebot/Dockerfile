FROM ruby:2.7

RUN \
    apt-get update && \
    apt-get install -y mpd mpc libopus-dev
RUN apt-get clean
COPY mpd.conf /etc/
RUN mkdir -p /run/mpd
RUN mkdir -p /var/lib/mpd
RUN mkdir -p /var/lib/mpd/tmp

COPY Gemfile .
COPY Gemfile.lock .
RUN bundle
COPY tls_version_patch.diff .
RUN patch /usr/local/bundle/gems/mumble-ruby-1.1.3/lib/mumble-ruby/connection.rb < /tls_version_patch.diff
COPY mumblebot.rb .

CMD ./mumblebot.rb
