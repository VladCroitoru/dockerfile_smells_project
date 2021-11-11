FROM ruby:2.4.2-slim-stretch
MAINTAINER Kenny Bergquist <bergquist.kenneth@gmail.com>

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get install -yq \
    build-essential zlib1g-dev libreadline6-dev libyaml-dev libssl-dev \
    locales \
    git apt-transport-https \
    ca-certificates \
    curl \
    gnupg2 \
    software-properties-common
RUN curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo "$ID")/gpg | apt-key add -
RUN add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") \
   $(lsb_release -cs) \
   stable"
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -yq docker-ce
## set the locale so gems built for utf8
RUN dpkg-reconfigure locales && \
    locale-gen C.UTF-8 && \
    /usr/sbin/update-locale LANG=C.UTF-8
ENV LC_ALL C.UTF-8

## help docker cache bundle
WORKDIR /tmp
COPY ./Gemfile /tmp/
COPY ./Gemfile.lock /tmp/

RUN bundle install

WORKDIR /app
COPY ./ /app

EXPOSE 5000

ENTRYPOINT [ "bundle", "exec" ]
CMD [ "foreman", "start" ]
