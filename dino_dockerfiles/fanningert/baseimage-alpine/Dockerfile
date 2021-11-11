FROM alpine:3.7
MAINTAINER ajoergensen

COPY files/repositories /etc/apk/repositories

ENV LANG='en_US.UTF-8' LANGUAGE='en_US.UTF-8' TERM='xterm' 

ARG BUILD_DATE
ARG VCS_REF
LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url="https://github.com/ajoergensen/baseimage-alpine.git" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.schema-version="1.0.0-rc1"

RUN apk update
RUN apk add rsyslog busybox-extras bash bash-completion bind-tools ssmtp curl file wget tar ca-certificates shadow tzdata jq && \
	cp /usr/share/zoneinfo/Europe/Copenhagen /etc/localtime && \
        apk add nano && \
        apk add screen && \
	apk del tzdata && \
	curl -sSL `curl -s https://api.github.com/repos/just-containers/s6-overlay/releases/latest | grep 'browser_' | cut -d\" -f4 | grep "s6-overlay-amd64.tar.gz$"` | tar xvfz - -C / && \
	wget -qO - https://github.com/jwilder/dockerize/releases/download/v0.5.0/dockerize-linux-amd64-v0.5.0.tar.gz | tar zxf - -C /usr/local/bin && \
	groupadd -g 911 app && \
	useradd -u 911 -g 911 -s /bin/false -m app && \
        usermod -G users app && \
	mkdir -p /app /config /defaults && \
	rm -rf /var/cache/apk/* /etc/rsyslog.conf

# Clean up apk cache
RUN rm -rf /var/cache/apk/*

ADD root /

RUN chmod -v +x /etc/cont-init.d/*

VOLUME ["/config"]

ENTRYPOINT ["/init"]
CMD []
