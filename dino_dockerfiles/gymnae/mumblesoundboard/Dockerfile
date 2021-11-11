# Mumble soundboard (MSB)
# go version
#
# This image makes use of the following software:
#
# 1. gomumblesoundboard base by: https://github.com/robbi5/gomumblesoundboard
#		The MIT License (MIT)
# 2. Webserver integration inspired by: https://github.com/gigablah/alpine-php
#		The MIT License (MIT)	
# 3. File manager: ELfinder - http://elfinder.org/#elf_l1_Lw
# 		Copyright (c) 2009-2016, Studio 42
#		All rights reserved.
# 4. Additional web code by #freaks on EFnet
#
# Please note the comments in this Docker file for running a container properly
#
#

FROM gymnae/alpine-base:latest

MAINTAINER      Gunnar Falk <docker@grundstil.de>
LABEL Description="This image allows you to use play your sound files in a mumble channel through a client controlled via web interface"

# Install dependencies
RUN set -ex && \
                # packages for gomumblesoundboard
                apk add --update tmux ffmpeg musl-dev opus go@community gcc git pkgconf opus-dev \
                # packages for the web facing side of this image
                php5 php5-pdo php5-sqlite3 php5-pdo_sqlite php5-fpm php5-json php5-ctype php5-curl php5-openssl nginx ca-certificates \
                # everyone is doing this. why?
            	&& rm -rf /var/cache/apk/*

# start getting going (hah)
WORKDIR /go

## for gomumblesoundboard
# Install go dep, download source files, change, and install
RUN export GOPATH=/go && \
        go get github.com/tools/godep/ && \
        git clone https://github.com/robbi5/gomumblesoundboard && \
        cp bin/godep gomumblesoundboard/ && \
        rm -R src pkg bin && \
        chmod 777 gomumblesoundboard && \
        cd gomumblesoundboard && \
        ./godep restore &&  \
        go build

#Remove packages for space saving - I'm sure I could squeeze out more
RUN apk del --update gcc git opus-dev musl-dev pkgconf && \
        rm -rf /var/cache/apk/*

## Mount msb-sounds folder - user action required
# It's recommended that you mount a host folder or docker volume with sound files.
# 
# Your local volume / data container is expected to have /sounds and /db as subfolders
# mount on docker run: -v <path on host / docker volume>:/media/msb 
# put your audio files into /sounds, the /db file can be generated as described above
VOLUME ["/media/msb/"]

# copy webserver config & content into container
COPY /webserver/config /

# mount webserver www folder
VOLUME /opt/www

# copy static copy of setup into container
# dirt hack maybe, but avoiding complicated download of a new file manager
COPY /webserver/code /opt/www

# Prepare the script that starts it all
ADD init.sh /
RUN chmod +x /init.sh && chmod 777 /init.sh

# define environment variables - default to them if nothing is declared on runtime
# ENV
ENV mumble_server=${mumble_server:-$MUMBLE_SERVER_PORT_64738_TCP_ADDR} \
 mumble_server_port=${mumble_server_port:-$MUMBLE_SERVER_PORT_64738_TCP_PORT} \
 mumble_server_channel=${mumble_server_channel:-Root} \
 mumble_user=${mumble_user:-spammer} \
 mumble_password=${mumble_password:-}

## Expose the port for the webserver - user action required
# Call the site with port 3000 for the raw gomumblesoundboard output
# Start the container with, e.g. -p 3001:80 if other web services are running on the 
# host 
EXPOSE 80 3000

#change to gomumblesoundboard for easy command start
WORKDIR gomumblesoundboard

# start
CMD ["/init.sh"]

