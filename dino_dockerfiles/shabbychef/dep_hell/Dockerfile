# TITLE
#
# docker build --rm -t shabbybanks/dep-hell .
#
# VERSION 0.1

FROM continuumio/anaconda

MAINTAINER Shabb E. Banks

ENV DOCKFILE_REFRESHED_AT 2017.06.21

RUN (conda update conda; \
	conda update --all ; \
	conda install -v -c conda-forge make=4.2.1 ; \
	conda install -c r r-base=3.2.2 ; \
	DEBIAN_FRONTEND=noninteractive DEBCONF_NONINTERACTIVE_SEEN=true apt-get install -y --no-install-recommends -q gcc libc-dev gfortran ; \
	ln -s /bin/tar /bin/gtar ; \
	mkdir -p /opt ;)

WORKDIR /opt
ADD .Rprofile /opt/
# this will install the packages brought in by the .Rprofile:
# but since no lockfile yet, it still runs:
RUN R -e 'rnorm(1)'

ADD lockfile.yml /opt/

ENTRYPOINT ["R"]

#for vim modeline: (do not edit)
# vim:nu:fdm=marker:fmr=FOLDUP,UNFOLD:cms=#%s:syn=Dockerfile:ft=Dockerfile:fo=croql
