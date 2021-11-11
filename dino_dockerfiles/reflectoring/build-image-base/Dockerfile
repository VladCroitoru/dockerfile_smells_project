FROM alpine:3.5

LABEL maintainer "matthias.balke@googlemail.com"

# check which package provides which command
# https://pkgs.alpinelinux.org/contents
RUN apk --no-cache add \
    "git=2.11.1-r0" \
    "openssh=7.4_p1-r0" \
    "bash=4.3.46-r5" \
    "curl=7.52.1-r2" \
    "ca-certificates=20161130-r1" \
    "openssl=1.0.2k-r0" \
    "ncurses=6.0-r7" \
    "coreutils=8.26-r0" \
    "make=4.2.1-r0" \
    "gcc=6.2.1-r1" \
    "g++=6.2.1-r1" \
    "libgcc=6.2.1-r1" \
    "linux-headers=4.4.6-r1" \
    "shadow=4.2.1-r7"

# make bash the default shell
RUN chsh -s /bin/bash
