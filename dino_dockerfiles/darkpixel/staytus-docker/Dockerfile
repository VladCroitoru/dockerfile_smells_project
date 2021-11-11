FROM ruby:2.7.0-alpine
LABEL org.opencontainers.image.source https://github.com/darkpixel/staytus-docker

RUN apk add --update --no-cache libc-dev make g++ nodejs tzdata curl mariadb-dev gettext libxml2-dev patch git ruby-dev
#RUN apt-get update && apt-get install -y gettext && apt-get clean
RUN mkdir  /app
WORKDIR /app

ENV RAILS_ENV=production
ENV RAILS_MAX_THREADS=1
ENV WEB_CONCURRENCY=1
#ENV BUNDLE_FROZEN=1
ENV BUNDLE_WITHOUT=development:test
#ENV BUNDLE_DISABLE_SHARED_GEMS=true
ENV BUNDLE_PATH=/app/vendor
ENV GEM_PATH="/app/gems"
ENV GEM_HOME="/app/gems"
ENV PATH $GEM_HOME/bin:$GEM_HOME/gems/bin:$PATH

RUN git clone https://github.com/adamcooke/staytus.git /app
#RUN git config advice.detachedHead=false
RUN git checkout b9b17f2966e3d659fda7d8114fbce9f384a72ef9
RUN gem install bundler:1.17.2
RUN bundle install --deployment
RUN gem install annotate:3.1.1

COPY docker-start-v2.sh /app/docker-start-v2.sh
COPY config/database.example.yml /app/config/database.example.yml
COPY config/environment.example.yml /app/config/environment.example.yml
COPY *.patch /app/


ENTRYPOINT /app/docker-start-v2.sh
EXPOSE 5000
