FROM olbat/docker-debian-ruby
MAINTAINER devel@olbat.net

RUN mkdir /src
COPY . /src

WORKDIR /src
ENTRYPOINT for f in */*.md; do ./md2bb < $f > ${f%.md}.bb; done
VOLUME ["/src"]
