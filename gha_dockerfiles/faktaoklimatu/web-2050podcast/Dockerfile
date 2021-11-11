FROM ubuntu:focal

LABEL name="2050 podcast" \
      summary="Jekyll deployment with Inkscape and ImageMagic for the 2050podcast.cz website" \
      usage="docker run --name 2050web -p 4000:4000 -v $PWD/..:/srv/jekyll -it 2050podcast"

ARG DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install --assume-yes software-properties-common
RUN add-apt-repository --yes ppa:inkscape.dev/stable && apt update
RUN apt install --assume-yes --no-install-suggests --no-install-recommends \
        build-essential git inkscape ruby-bundler ruby-dev zlib1g-dev libffi-dev imagemagick

EXPOSE 4000
VOLUME /srv/jekyll
WORKDIR /srv/jekyll

CMD ["make", "local"]
