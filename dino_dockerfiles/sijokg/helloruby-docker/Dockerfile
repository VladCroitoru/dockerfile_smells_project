#A hello world example using Ruby
FROM ruby:2.4.1
MAINTAINER "sijo.george.ap@nielsen.com"
ENV APPROOT="/app" \
    APP="hello.rb"
WORKDIR $APPROOT
COPY ["./source-dir/hello.rb", "${APPROOT}"]
CMD ruby $APP
