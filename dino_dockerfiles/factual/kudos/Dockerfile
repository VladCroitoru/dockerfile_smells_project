FROM ruby:2.5

# Install node, s3cmd, postgresql-client
RUN echo 'deb http://apt.postgresql.org/pub/repos/apt/ stretch-pgdg main' > /etc/apt/sources.list.d/pgdg.list
RUN curl -s https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get update -y && \
    apt-get install -y nodejs \
                       build-essential \
                       s3cmd \
                       postgresql-client-10

WORKDIR /usr/src/app

COPY Gemfile /usr/src/app/
COPY Gemfile.lock /usr/src/app/
RUN bundle install

COPY client/package.json /usr/src/app/client/
COPY client/package-lock.json /usr/src/app/client/
RUN cd client && npm install

COPY . /usr/src/app
