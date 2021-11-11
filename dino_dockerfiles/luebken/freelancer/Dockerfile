# https://registry.hub.docker.com/_/ruby/
FROM ruby:2.1.2

RUN  apt-get update && \
	 apt-get -y install nodejs

RUN gem install jekyll

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
ADD . /usr/src/app

EXPOSE 4000

ONBUILD COPY _config.yml /usr/src/app/
ONBUILD COPY _posts /usr/src/app/_posts/
ONBUILD COPY img /usr/src/app/img/

CMD ["jekyll", "serve"]