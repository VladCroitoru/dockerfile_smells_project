FROM	docker.io/rootwyrm/tc_docker:latest
MAINTAINER	Phillip "RootWyrm" Jaenke <talecaster@rootwyrm.com>

## Set up our labels
ARG RW_BLDHASH
ARG RW_VCSHASH
ARG RW_VCSBRANCH
ARG LS_VCSREF
ARG LS_BLDDATE
ARG LS_VENDOR
ARG LS_SCHEMA
ARG LS_SCHEMAVERSION
ARG LS_NAME
ARG LS_URL

LABEL	com.rootwyrm.product="TaleCaster" \
		com.rootwyrm.project="tc_transmission" \
		com.rootwyrm.status="" \
		com.rootwyrm.vcs-type="github" \
		com.rootwyrm.changelog-url="https://github.com/rootwyrm/talecaster/CHANGELOG" \
		com.rootwyrm.nvd.release="0" \
		com.rootwyrm.nvd.version="0" \
		com.rootwyrm.nvd.update="0" \
		com.rootwyrm.nvd.update_sub="$RW_VCSHASH" \
		com.rootwyrm.nvd.build_time="$LS_BLDDATE" \

		com.rootwyrm.talecaster.provides="bittorrent" \
		com.rootwyrm.talecaster.depends="" \
		com.rootwyrm.talecaster.service="transmission" \
		com.rootwyrm.talecaster.ports_tcp="9091" \
		com.rootwyrm.talecaster.ports_udp="9091 43454" \
		com.rootwyrm.talecaster.synology="0" \
		com.rootwyrm.talecaster.qnap="0" \

		org.label-schema.schema-version="$LS_SCHEMAVERSION" \
		org.label-schema.vendor="$LS_VENDOR" \
		org.label-schema.name="$LS_NAME" \
		org.label-schema.url="$LS_URL" \
		org.label-schema.vcs-ref="$VCS_REF" \
		org.label-schema.version="$RW_BLDHASH" \
		org.label-schema.build-date="$LS_BLDDATE"

## PORTS
EXPOSE	9091/tcp 9091/udp 43454/udp

## Common Components
COPY [ "application/", "/opt/talecaster" ]
COPY [ "sv/", "/etc/sv" ]

## Application and Supporting Tools
ENV pkg_application="transmission-daemon"
RUN apk add --no-cache $pkg_application

ADD	README.md /README.md

## Reset state on build
ONBUILD CMD touch /firstboot

## Terminus
CMD [ "/sbin/runsvdir", "-P", "/etc/service" ]
