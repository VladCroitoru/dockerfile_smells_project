#
# dockerfile for qbound paper
#
# docker build --rm -t shabbychef/qbound .
#
# docker run -it --rm --volume $(pwd):/srv:rw shabbychef/qbound
#
# Created: 2018.05.08
# Copyright: Steven E. Pav, 2018
# Author: Steven E. Pav
# Comments: Steven E. Pav

#####################################################
# preamble# FOLDUP
FROM shabbychef/knitrer
MAINTAINER Steven E. Pav, shabbychef@gmail.com
# UNFOLD

ENV DOCKERFILE_REFRESHED_AT 2018.05.08

RUN (apt-get clean -y ; \
  apt-get update -y -qq; \
  apt-get update --fix-missing ; \
  DEBIAN_FRONTEND=noninteractive DEBCONF_NONINTERACTIVE_SEEN=true apt-get install -q -y --no-install-recommends libblas-dev ; \
  sync ; \
  mkdir -p /usr/local/lib/R/site-library ; \
  chmod -R 777 /usr/local/lib/R/site-library ; \
  sync ; \
  /usr/local/bin/install2.r remotes knitr devtools doFuture doRNG dplyr ggplot2 hypergeo knitr LambertW quantmod SharpeR tidyr xtable ; \
  /usr/local/bin/installGithub.r "shabbychef/aqfb_data" )

ADD Makefile /srv/ 
ADD qbound.Rnw /srv/ 
ADD qbound.R /srv/ 
ADD *.bib /srv/ 
ADD *.sty /srv/ 
ADD sp100lr.rda /srv/ 

RUN mkdir -p /srv/cache /srv/figure ;

RUN mkdir -p /srv/Definitions 
ADD mdpi.Rnw /srv/ 
ADD Definitions/* /srv/Definitions/

# larger values build the doc quicker with lower resolution simulations.
ENV RUNTIME_PARAM 1

#RUN groupadd -g 1000 spav && useradd -g spav -u 1000 spav;
#USER spav

#####################################################
# entry and cmd# FOLDUP
# these are the default, but remind you that you might want to use /usr/bin/R instead?
# always use array syntax:
# fix these.
#ENTRYPOINT ["/usr/local/bin/R","CMD","check","--as-cran","--output=/tmp"]
ENTRYPOINT ["/bin/bash"]

# ENTRYPOINT and CMD are better together:
CMD ["-i"]
# UNFOLD

#for vim modeline: (do not edit)
# vim:et:nu:fdm=marker:fmr=FOLDUP,UNFOLD:cms=#%s:syn=Dockerfile:ft=Dockerfile:fo=croql
