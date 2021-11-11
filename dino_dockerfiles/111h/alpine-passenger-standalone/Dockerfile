FROM ruby:2.3.1-alpine

ARG PACKAGES="make gcc g++ musl-dev curl libexecinfo nodejs"
ENV APP_PATH /usr/src/app

ENV PATH="/opt/passenger/bin:$PATH"

RUN mkdir -p /opt/passenger
COPY passenger /opt/passenger

RUN echo 'http://dl-cdn.alpinelinux.org/alpine/edge/main/' >> /etc/apk/repositories
 
# default packages
RUN apk --no-cache add $PACKAGES

#app dir
RUN mkdir -p $APP_PATH
WORKDIR $APP_PATH

######################################### example rack app
RUN gem install rack
COPY config.ru /usr/src/app/

CMD ["passenger", "start", "--no-install-runtime", "--no-compile-runtime"]
EXPOSE 3000
