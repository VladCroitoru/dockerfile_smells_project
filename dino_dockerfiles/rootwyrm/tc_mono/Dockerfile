FROM	docker.io/rootwyrm/tc_docker:latest
MAINTAINER	Phillip "RootWyrm" Jaenke <talecaster@rootwyrm.com>

LABEL	com.rootwyrm.product="TaleCaster" \
		com.rootwyrm.project="tc_mono" \
		com.rootwyrm.status="" \
		com.rootwyrm.vcs-type="github" \
		com.rootwyrm.changelog-url="https://github.com/rootwyrm/talecaster/CHANGELOG" \
		com.rootwyrm.nvd.release="0" \
		com.rootwyrm.nvd.version="0" \
		com.rootwyrm.nvd.update="0" \
		com.rootwyrm.nvd.update_sub="$RW_VCSHASH" \
		com.rootwyrm.nvd.build_time="$LS_BLDDATE" \

		com.rootwyrm.talecaster.provides="mono" \
		com.rootwyrm.talecaster.depends="" \
		com.rootwyrm.talecaster.service="" \
		com.rootwyrm.talecaster.ports_tcp="" \
		com.rootwyrm.talecaster.ports_udp="" \
		com.rootwyrm.talecaster.synology="0" \
		com.rootwyrm.talecaster.qnap="0" \

		org.label-schema.schema-version="$LS_SCHEMAVERSION" \
		org.label-schema.vendor="$LS_VENDOR" \
		org.label-schema.name="$LS_NAME" \
		org.label-schema.url="$LS_URL" \
		org.label-schema.vcs-ref="$VCS_REF" \
		org.label-schema.version="$RW_BLDHASH" \
		org.label-schema.build-date="$LS_BLDDATE"

## Create common elements
COPY [ "application/", "/opt/talecaster" ]

RUN echo "$(date '+%b %d %H:%M:%S') [RUN] phase beginning." ; \
	mkdir -p /opt/talecaster/build && \
	mkdir -p /var/log/runit && \
	touch /firstboot && \
	apk update && \
	apk upgrade && \
	for bld in `ls /opt/talecaster/build/ | sort`; do \
		/opt/talecaster/build/$bld ; \
	done && \
	echo "$(date '+%b %d %H:%M:%S') [RUN] phase complete."
	
VOLUME [ "/run", "/shared" ]

## Handle rebuilds in a nicer fashion.
ONBUILD RUN apk update ; apk upgrade
