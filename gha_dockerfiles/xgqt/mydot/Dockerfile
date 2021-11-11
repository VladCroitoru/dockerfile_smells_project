# This file is part of mydot.

# mydot is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.

# mydot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with mydot.  If not, see <https://www.gnu.org/licenses/>.

# Copyright (c) 2021, Maciej Barć <xgqt@riseup.net>
# Licensed under the GNU GPL v3 License

# docker build -t mydot .
# docker image ls
# docker run -it ID bash
# export TERM=xterm-256color
# emacs -nw


FROM alpine:3.13.5

LABEL maintainer "Maciej Barć <xgqt@riseup.net>"


ENV SHELL=bash
ENV TERM=dumb

RUN apk add bash busybox emacs-nox git make ncurses shellcheck stow zsh

RUN mkdir -p /opt/mydot
COPY ./ /opt/mydot


# Tests & cleanup for installation
RUN cd /opt/mydot  && \
    make test-shellcheck  && \
    make test-emacs  && \
    make remove-blockers

# Install MyDot
RUN /opt/mydot/stowdot
