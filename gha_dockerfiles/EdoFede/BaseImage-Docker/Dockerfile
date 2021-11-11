ARG BASEIMAGE_BRANCH
FROM alpine:$BASEIMAGE_BRANCH

# Install required software
RUN	apk update && \
	apk --no-cache add \
		bash \
		curl \
		nano \
		runit \
		syslog-ng \
		tzdata \
		unzip \
		vim && \
	rm -rf /var/cache/apk/* && \
# Set local timezone
	cp /usr/share/zoneinfo/Europe/Rome /etc/localtime

COPY imageFiles/ /

RUN chmod +x /entrypoint.sh && \
	chmod +x /etc/runit/1 /etc/runit/2 /etc/runit/3 && \
	chmod +x /etc/sv/syslog-ng/run && \
	ln -sf /etc/sv/syslog-ng /etc/service/ && \
	ln -sf /etc/sv/postScripts-handler /etc/service/ && \
	sed -i "s/^\(tty\d\:\:\)/#\\1/g" /etc/inittab

ARG BUILD_DATE
ARG VERSION
ARG VCS_REF

LABEL 	maintainer="Edoardo Federici <hello@edoardofederici.com>" \
		org.label-schema.schema-version="1.0.0-rc.1" \
		org.label-schema.vendor="Edoardo Federici" \
		org.label-schema.url="https://edoardofederici.com" \
		org.label-schema.name="baseimage" \
		org.label-schema.description="Docker multiarch base image with runit, syslog-ng and few tools" \
		org.label-schema.version=$VERSION \
		org.label-schema.build-date=$BUILD_DATE \
		org.label-schema.vcs-url="https://github.com/EdoFede/BaseImage-Docker" \
		org.label-schema.vcs-ref=$VCS_REF \
		org.label-schema.docker.cmd="docker create --name BaseImage edofede/baseimage:latest"

STOPSIGNAL SIGCONT

ENTRYPOINT ["/entrypoint.sh"]
