FROM alpine
MAINTAINER Sven Dowideit <SvenDowideit@home.org.au>

ADD bootstrap.sh /
ADD install/ /install/

# Sorry, I'm doing development on windows
RUN chmod 755 /bootstrap.sh \
	&& chmod 755 /install/*

ENTRYPOINT ["/bootstrap.sh"]
