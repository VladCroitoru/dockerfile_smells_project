FROM alpine:3.2  
MAINTAINER technolengy@gmail.com

RUN apk update && apk --update add ruby ruby-irb ruby-io-console tzdata

ADD Gemfile /app/  
ADD Gemfile.lock /app/

RUN apk --update add --virtual build-deps build-base ruby-dev \
    && gem install bundler --no-ri --no-rdoc \
    && cd /app \
    && bundle install \
    && apk del build-deps

ADD . /app  
RUN chown -R nobody:nogroup /app  
USER nobody

ENV RAILS_ENV production  
WORKDIR /app

EXPOSE 5000

CMD ["bundle", "exec", "ruby", "pw.rb","-p", "5000"] 