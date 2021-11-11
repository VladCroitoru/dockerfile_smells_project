#
# word2vec i docker.
#
# VERSION 0.1
#
# docker build --rm -t shabbychef/word2vec .
#
# Created: 2015.10.14
# Copyright: Steven E. Pav, 2015
# Author: Steven E. Pav
# Comments: Steven E. Pav

#####################################################
# preamble# FOLDUP
FROM ubuntu:14.04
MAINTAINER Steven E. Pav, shabbychef@gmail.com
USER root
# UNFOLD

#####################################################
# update ubuntu, install packages, and so on
RUN (rm -rf /var/lib/apt/lists/* ; \
 apt-get clean -y ; \
 apt-get update -y -qq; \
 apt-get update --fix-missing ; \
 DEBIAN_FRONTEND=noninteractive DEBCONF_NONINTERACTIVE_SEEN=true apt-get install -y --no-install-recommends -q build-essential ; \
 apt-get clean -q -y )

RUN mkdir -p /opt/word2vec

ADD src/ /opt/word2vec/

WORKDIR /opt/word2vec

RUN make all

WORKDIR /tmp

#####################################################
# entry and cmd# FOLDUP
# always use array syntax:

ENTRYPOINT ["/opt/word2vec/word2vec"]

# ENTRYPOINT and CMD are better together:
CMD []
# UNFOLD

#for vim modeline: (do not edit)
# vim:nu:fdm=marker:fmr=FOLDUP,UNFOLD:cms=#%s:syn=Dockerfile:ft=Dockerfile:fo=croql
