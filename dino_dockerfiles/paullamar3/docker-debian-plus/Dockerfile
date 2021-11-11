## Dockerfile for "base" Debian image.
## This image contains some utilities that I can reuse in images
## derived from it.
FROM debian:jessie
MAINTAINER Paul LaMar <pal3@outlook.com>

# Set language to UTF-8
ENV LANG    C.UTF-8

# Set TERM to XTERM
ENV TERM    xterm

# Add utility scripts: p_addpkgs, p_adduser
COPY clocal/p_* clocal/gosu /usr/local/bin/
RUN chmod +x /usr/local/bin/p_* /usr/local/bin/gosu

