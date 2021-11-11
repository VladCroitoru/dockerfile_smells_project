FROM debian:7

RUN apt-get update -qq && \
    apt-get -y install curl && \
    apt-get clean -y && \
    rm -rf /var/cache/apt/*

RUN curl -sSL -o /tmp/hugo.deb https://github.com/spf13/hugo/releases/download/v0.15/hugo_0.15_amd64.deb && \
    dpkg -i /tmp/hugo.deb && rm /tmp/hugo.deb

RUN mkdir -p /srv/blog
COPY . /srv/blog
VOLUME /var/www/shanesveller.com
CMD ["hugo","-t","hugo-redlounge","-s","/srv/blog","-d","/var/www/shanesveller.com"]
