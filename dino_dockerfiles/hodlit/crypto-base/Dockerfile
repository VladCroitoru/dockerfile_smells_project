FROM alpine:3.7
# Build-time metadata as defined at http://label-schema.org
ARG BUILD_DATE
ARG VCS_REF
ARG VERSION
LABEL org.label-schema.build-date=$BUILD_DATE \
			org.label-schema.name="HODLit 3DCoin Miner" \
			org.label-schema.description="Solo CPU mining for 3DCoin" \
			org.label-schema.url="hodlit.io" \
			org.label-schema.vcs-ref=$VCS_REF \
			org.label-schema.vcs-url="https://github.com/HODLit-3dcoin/3dcoin-miner" \
			org.label-schema.vendor="Varts" \
			org.label-schema.version=$VERSION \
			org.label-schema.schema-version="1.0"

RUN set -x && \
addgroup -g 1000 -S crypto && \
adduser -u 1000 -S crypto -G crypto && \
apk add --no-cache tini su-exec && \
chown -R crypto:crypto /home/crypto && \
cd /home/crypto && \
echo '#!/bin/sh' > entrypoint.sh && \
echo '' >> entrypoint.sh && \
echo 'echo "user params count: $#"' >> entrypoint.sh && \
echo 'echo "user params: $@"' >> entrypoint.sh && \
echo '' >> entrypoint.sh && \
echo 'if [[ $# -lt 1 ]] || [[ "$1" == "-"* ]]; then' >> entrypoint.sh && \
	echo 'echo "Sleeping.  Pid=$$"' >> entrypoint.sh && \
	echo 'while true; do' >> entrypoint.sh && \
		echo 'sleep 10 &' >> entrypoint.sh && \
		echo 'wait $!' >> entrypoint.sh && \
		echo 'echo "Zzz..."' >> entrypoint.sh && \
	echo 'done' >> entrypoint.sh && \
echo 'fi' >> entrypoint.sh && \
echo '' >> entrypoint.sh && \
echo 'su-exec crypto "$@"' >> entrypoint.sh && \
echo '' >> entrypoint.sh && \
chmod a+x entrypoint.sh

WORKDIR /home/crypto
ENTRYPOINT ["/sbin/tini", "--", "/home/crypto/entrypoint.sh"]
