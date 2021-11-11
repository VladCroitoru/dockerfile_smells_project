FROM ruby:2.3.3

WORKDIR /app

RUN curl -sL https://deb.nodesource.com/setup_13.x -o nodesource_setup.sh  && \
    bash nodesource_setup.sh
RUN apt install -y \
      ruby-dev \
      build-essential \
      libgmp-dev \
      git

# Copy Ruby and Node dependencies
COPY Gemfile Gemfile.lock package.json package-lock.json ./

RUN gem install bundler:1.17.3
# Install dependencies
RUN bundle install --without debug
RUN apt-get install -y --force-yes nodejs && npm install

# Fix hosts file
EXPOSE 4567
