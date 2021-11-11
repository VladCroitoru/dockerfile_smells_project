FROM ruby
MAINTAINER Markus Benning <ich@markusbenning.de>

WORKDIR /usr/src/app
COPY Gemfile* ./
RUN bundle install
COPY . .

ADD mcollective/client.cfg /root/.mcollective
ADD mcollective/prometheus.ddl /opt/puppetlabs/mcollective/plugins/mcollective/agent/prometheus.ddl

EXPOSE 80

CMD bundle exec unicorn -c unicorn.rb

