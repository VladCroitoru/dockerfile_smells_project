FROM ubuntu:14.04
MAINTAINER Sascha Ishikawa <sascha@zooniverse.org>
WORKDIR /planetary-response-network
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get -y upgrade && \
    apt-get install --no-install-recommends -y ca-certificates sudo git curl bash-completion vim-tiny supervisor ghostscript imagemagick libgdal-dev libimage-exiftool-perl make g++ python
RUN curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash -
RUN apt-get install --no-install-recommends -y nodejs && apt-get clean

# Language setup
RUN locale-gen  fr_FR.UTF-8 en_US.UTF-8
RUN update-locale LANG=en_US.UTF-8

# Common alias
RUN alias ls='ls --color=auto'
RUN alias ll='ls -halF'

ADD supervisord.conf /etc/supervisor/supervisord.conf
ADD ./ /planetary-response-network

RUN npm install .

EXPOSE 3736
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]
# CMD ["echo", "hello there!"]

# # Gdal binary crashes on mac VM, so build from scratch by running this on the instance:
# apt-get install --no-install-recommends -y libgdal-dev && \
#   npm install gdal --build-from-source --shared_gdal
