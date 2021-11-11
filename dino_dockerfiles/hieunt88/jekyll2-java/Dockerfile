FROM jekyll/jekyll:2.5.3
RUN printf "\nhttp://dl-4.alpinelinux.org/alpine/v3.3/community" >> /etc/apk/repositories \
	&& apk add --update openjdk7-jre \
	&& rm -rf /tmp/* \
  && rm -rf /var/cache/apk/* \