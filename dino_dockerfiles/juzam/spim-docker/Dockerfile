FROM debian:jessie
MAINTAINER jan@jangmarker.de

RUN	apt-get update && apt-get --yes --no-install-recommends install \
	bison \
	build-essential \
	flex \
	subversion

WORKDIR /spim

ADD ./diff_to_spim_for_large_projects.diff spim.diff

RUN	svn checkout svn://svn.code.sf.net/p/spimsimulator/code/ spim-code

WORKDIR /spim/spim-code/spim

RUN patch -Np1 < ../../spim.diff

RUN make -j5 && make -j5 install

ENTRYPOINT ["/usr/bin/spim"]