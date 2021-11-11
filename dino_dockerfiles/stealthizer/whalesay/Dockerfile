FROM alpine:latest
MAINTAINER stealthizer - https://github.com/stealthizer

# Install Perl
RUN apk update && apk add --no-cache perl

# Overwrite the default cow template with the whale one

COPY cowsay /usr/local/bin/cowsay
RUN chmod 766  /usr/local/bin/cowsay
COPY docker.cow /usr/local/share/cows/default.cow

ENTRYPOINT ["/usr/local/bin/cowsay"]
