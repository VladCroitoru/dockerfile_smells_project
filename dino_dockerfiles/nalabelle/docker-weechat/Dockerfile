FROM lsiobase/alpine:3.7

RUN \
 echo "**** install app ****" && \
 apk add --no-cache \
  weechat \
  weechat-python \
  weechat-perl \
  python \
  tmux && \
 echo "You may want to install: weechat-lua lua5.3 weechat-ruby ruby" && \
 echo "**** clean up ****" && \
 rm -rf \
	/root/.cache \
	/tmp/*

COPY root/ /

EXPOSE 9001

VOLUME /config
