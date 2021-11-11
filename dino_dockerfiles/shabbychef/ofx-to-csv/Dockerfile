# TITLE
#
# VERSION 0.1
#
# docker build --rm -t shabbychef/ofx .
# docker run -it --rm -v $(pwd):/srv:rw --entrypoint="/bin/bash" shabbychef/ofx "-i"
# ./ofx-to-csv.rb ./Accounts.20170131_214525.OFX  > /srv/transactions.csv 
#
# SVN: $Id$
# Created: 2017.02.01
# Copyright: Steven E. Pav, 2017
# Author: Steven E. Pav
# Comments: Steven E. Pav

#FROM ruby:2-onbuild 
FROM ruby:2.4

MAINTAINER Steven E. Pav, steven@gilgamath.com

ENV DOCKFILE_REFRESHED_AT 2017.02.01
ENV NONCE e6bcf268-4a06-4921-9ae9-9cb722154789

RUN mkdir -p /usr/src/app;
WORKDIR /usr/src/app

COPY Gemfile /usr/src/app/
COPY . /usr/src/app

# throw errors if Gemfile has been modified since Gemfile.lock
#RUN (bundle config --global frozen 1 ; \
#bundle install )

RUN bundle install 

# always use array syntax:
ENTRYPOINT ["/usr/src/app/ofx-to-csv.rb"]
# ENTRYPOINT and CMD are better together:
CMD ["-h"]

#for vim modeline: (do not edit)
# vim:nu:fdm=marker:fmr=FOLDUP,UNFOLD:cms=#%s:syn=Dockerfile:ft=Dockerfile:fo=croql
