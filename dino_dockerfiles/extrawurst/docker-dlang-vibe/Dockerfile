FROM ubuntu:18.04
LABEL maintainer="extrawurst"
RUN apt-get update \
    && apt-get install -yy wget gcc libcurl3 git libevent-dev libssl1.0-dev libevent-pthreads-2.1-6
RUN wget http://downloads.dlang.org/releases/2.x/2.082.0/dmd_2.082.0-0_amd64.deb \
	&& dpkg -i /dmd_2.082.0-0_amd64.deb
RUN dmd --version \
    && dub --version
