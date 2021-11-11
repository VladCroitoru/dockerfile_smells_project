FROM ruby:2.6-alpine

STOPSIGNAL SIGKILL
ENV HTTP_PORT=80

RUN \
    gem install sinatra --no-document

COPY http-echo.rb /opt/http-echo.rb

EXPOSE 80
CMD \
    ruby /opt/http-echo.rb
