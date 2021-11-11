# Docker image for gollum wiki
# Based loosely on https://github.com/suttang/docker-gollum/blob/master/Dockerfile
FROM justbuchanan/docker-archlinux
MAINTAINER Justin Buchanan <justbuchanan@gmail.com>

RUN pacman -Sy --noconfirm ruby base-devel icu cmake

# Configure home and gem path for user dev
# TODO: don't hardcode version
ENV GEM_PATH "/root/.gem/ruby/2.3.0"
ENV PATH $PATH:$GEM_PATH/bin

RUN gem install gollum --no-ri --no-rdoc
RUN gem install gollum-rugged_adapter --no-ri --no-rdoc

# mount an external repo to this directory
RUN mkdir /root/wikidata

EXPOSE 4567

CMD ["gollum", "/root/wikidata", "--adapter", "rugged"]
