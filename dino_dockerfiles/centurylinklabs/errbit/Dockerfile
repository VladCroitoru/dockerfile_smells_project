FROM centurylink/ruby-base:2.1.2

MAINTAINER CenturyLink Labs <clt-labs-futuretech@centurylink.com>

# OS-Level dependencies
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \
  git \
  libxml2 \
  libxml2-dev \
  libxslt-dev \
  libcurl4-openssl-dev

# Setup environment
ENV RAILS_ENV production
ENV USE_ENV true

# Create errbit user
RUN /usr/sbin/useradd --create-home --home-dir /opt/errbit --shell /bin/bash errbit

# Get errbit code
ADD . /opt/errbit/app
RUN chown -R errbit:errbit /opt/errbit/app

# Set-up app
USER errbit
WORKDIR /opt/errbit/app
RUN bundle install --deployment
RUN bundle exec rake assets:precompile

EXPOSE 3000
CMD echo "Errbit::Application.config.secret_token = '$(bundle exec rake secret)'" > config/initializers/__secret_token.rb && \
  MONGODB_URL="$MONGODB_PORT/errbit" bundle exec rake db:seed && \
  MONGODB_URL="$MONGODB_PORT/errbit" bundle exec rake db:mongoid:create_indexes && \
  MONGODB_URL="$MONGODB_PORT/errbit" bundle exec unicorn -p 3000 -c ./config/unicorn.rb
