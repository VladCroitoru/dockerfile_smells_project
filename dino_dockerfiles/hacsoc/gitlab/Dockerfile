FROM gitlab/gitlab-ce

RUN apt-get update && apt-get install -y build-essential cmake libxml2 libxml2-dev zlib1g-dev

COPY Gemfile /opt/gitlab/embedded/service/gitlab-rails/
WORKDIR /opt/gitlab/embedded/service/gitlab-rails/

RUN bundle config build.nokogiri --use-system-libraries --with-xml2-include=/usr/include/libxml2
RUN bundle update && bundle install --without development test mysql

COPY gitlab.rb /etc/gitlab/
WORKDIR /
