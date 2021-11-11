FROM node:latest

LABEL maintainer="Tomohisa Kusano <siomiz@gmail.com>"

ENV OPENCV_VERSION 3.4.0

COPY build.sh /build.sh
RUN bash /build.sh \
	&& rm /build.sh

ENV LD_LIBRARY_PATH /usr/local/lib

CMD ["node"]
