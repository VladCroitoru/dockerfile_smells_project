FROM starbuildr/phoenix-new:1.0.2

MAINTAINER Vyacheslav Voronchuk <voronchuk@gmail.com>

RUN apt-get update
RUN apt-get install -y imagemagick
RUN apt-get install -y mysql-client

ARG MIX_ENV=prod
ENV MIX_ENV $MIX_ENV

WORKDIR /var/app

ENTRYPOINT ["mix", "phoenix.server"]