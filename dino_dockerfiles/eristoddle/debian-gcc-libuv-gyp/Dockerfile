FROM debian:8
#Install packages
RUN apt-get update -y \
	&& apt-get install -y gcc g++ libuv-dev make python git curl

#Install vanilla gyp because that's how I learned to compile C
RUN cd /tmp && curl https://bootstrap.pypa.io/ez_setup.py -o - | python \
	&& git clone https://chromium.googlesource.com/external/gyp.git \
	&& cd gyp \
 	&& python setup.py install \
 	&& cd .. \
 	&& rm -rf gyp

#Clean up
RUN cd /tmp \
 	&& rm -rf gyp \
 	&& apt-get remove -y git curl