FROM ruby:2.6-alpine
MAINTAINER Alexander Egorov <a.a.egoroff@gmail.com>

EXPOSE 5678
ENV RACK_ENV production
ENV RUBYOPT --jit

WORKDIR /app
COPY . /app
RUN /app/prepare.sh

CMD bundler exec rackup -o 0.0.0.0 -p 5678 -E ${RACK_ENV}
