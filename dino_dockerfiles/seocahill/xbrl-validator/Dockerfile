FROM jruby:9-alpine
MAINTAINER seo.cahill@gmail.com

# Install apt based dependencies required to run Rails as
# well as RubyGems. As the Ruby image itself is based on a
# Debian image, we use apt-get to install those.
# RUN apt-get update && apt-get install -y \
#   build-essential \
#   nodejs

# Configure the main working directory. This is the base
# directory used in any further RUN, COPY, and ENTRYPOINT
# commands.
RUN mkdir -p /app
WORKDIR /app

# Copy the Gemfile as well as the Gemfile.lock and install
# the RubyGems. This is a separate step so the dependencies
# will be cached unless changes to one of those two files
# are made.
RUN apk update && apk add nodejs
COPY Gemfile ./
# RUN apk --update add --virtual build_deps \
#     build-base ruby-dev libc-dev linux-headers \
#     libressl-dev libxml2-dev libxslt-dev \
    # apk del build_deps
RUN gem install bundler && bundle install --jobs 20 --retry 5

# Copy the main application.
COPY . ./

EXPOSE 4567

ENTRYPOINT ["jruby"]

CMD ["app.rb"]
