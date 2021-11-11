#
# shiny + onbuild directives.
#
# FROM littler 
# adds shiny and DT
#
# the ONBUILD directives first look for
# ./apt_packages.txt, with a package on each line,
# then attempts to apt-get install them.
# Lines in apt_packages.txt starting with '#' are comments, and are ignored.
#
# then looks for ./r_packages.txt, with an R package on each line,
# then attempts to rinstall2 them.
# Lines in r_packages.txt starting with '#' are comments, and are ignored.
#
# then looks for ./r_github_packages.txt, with an install_github package description
# on each line, then attempts to installGithub them. These should have the form
# 'username/repo[/subdir][@ref|#pull]'
# Lines in r_github_packages.txt starting with '#' are comments, and are ignored.
#
# then looks for src and ADDs it at /srv/shiny
# runs the app.
#
# VERSION 0.1
#
# docker build --rm -t shabbychef/shiny-onbuild .
#
# Created: 2016.02.09
# Copyright: Steven E. Pav, 2016
# Author: Steven E. Pav
# Comments: Steven E. Pav

#####################################################
# preamble# FOLDUP
FROM shabbychef/littler 
MAINTAINER Steven E. Pav, shabbychef@gmail.com
USER root
# UNFOLD

# get shiny and the latest, greatest DT:
RUN ( apt-get update -y -qq && apt-get install -y --no-install-recommends libxt-dev libcairo2-dev ; \
  /usr/local/bin/install.r shiny docopt Cairo ; \
  /usr/local/bin/installGithub.r 'rstudio/DT' ; \   
  useradd -U shiny ; \ 
  mkdir -p /srv/shiny ; \ 
  chown -R shiny:shiny /srv/shiny ; \
  chmod -R 755 /srv/shiny ; \
  mkdir -p /opt/shiny ; \
  apt-get -y clean ; \
	rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* )

ADD runapp.r /opt/shiny/

# just make sure it is fresh:
#RUN rm -rf /var/lib/apt/lists/* && apt-get clean -y && apt-get update -y -q;

#####################################################
# onbuild magic# FOLDUP
# c.f.
# http://docs.docker.com/engine/articles/dockerfile_best-practices/#build-cache
ONBUILD COPY ./*_packages.txt /tmp/

ONBUILD RUN DEBIAN_FRONTEND=noninteractive DEBCONF_NONINTERACTIVE_SEEN=true \
 [ -f /tmp/apt_packages.txt ] && grep -q -ve '^\s*#' /tmp/apt_packages.txt && \
 apt-get update -y -qq && apt-get install -y --no-install-recommends -q $(grep -ve '^\s*#' /tmp/apt_packages.txt) || true;

ONBUILD RUN [ -f /tmp/r_packages.txt ] && grep -q -ve '^\s*#' /tmp/r_packages.txt && \
 /usr/local/bin/install.r $(grep -ve '^\s*#' /tmp/r_packages.txt) || true;

ONBUILD RUN [ -f /tmp/r_github_packages.txt ] && grep -q -ve '^\s*#' /tmp/r_github_packages.txt && \
 /usr/local/bin/installGithub.r $(grep -ve '^\s*#' /tmp/r_github_packages.txt) || true;

ONBUILD ADD src/ /srv/shiny/
# UNFOLD

EXPOSE 5555

#####################################################
# entry and cmd# FOLDUP
# always use array syntax:
ENTRYPOINT ["/usr/bin/r","/opt/shiny/runapp.r","--host=0.0.0.0","--port=5555","--appdir=/srv/shiny"]

# ENTRYPOINT and CMD are better together:
CMD []
# UNFOLD

#for vim modeline: (do not edit)
# vim:nu:fdm=marker:fmr=FOLDUP,UNFOLD:cms=#%s:syn=Dockerfile:ft=Dockerfile:fo=croql
