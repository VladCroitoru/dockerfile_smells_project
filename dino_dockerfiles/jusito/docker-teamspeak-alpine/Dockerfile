FROM frolvlad/alpine-glibc:alpine-3.9_glibc-2.29

EXPOSE 9987/udp 10011/tcp 30033/tcp

ENV TS3SERVER_LICENSE="accept" \
	TS_DIR_NAME="teamspeak3-server" \
	TS_PATH="/home/teamspeak3-server" \
	TS_GROUP_ID=10002 \
	TS_USER_ID=10002 \
	TS_USER=teamspeak

COPY ["teamspeakUpdater.sh", "/home/teamspeakUpdater.sh" ]
	
RUN apk update && \
	apk add --no-cache ca-certificates libstdc++ && \
	addgroup -g "${TS_GROUP_ID}" "${TS_USER}" && \
	adduser -h "${TS_PATH}" -g "" -s "/bin/false" -G "${TS_USER}" -D -u "${TS_USER_ID}" "${TS_USER}" && \
	chown "$TS_USER" "/home/teamspeakUpdater.sh" && \
	chmod  u=rwx,go= "/home/teamspeakUpdater.sh" && \
	chown -R "$TS_USER" "$TS_PATH" && \
	chmod -R u=rwx,go= "$TS_PATH" && \
	apk del --quiet --no-cache --progress --purge && \
	rm -rf /var/cache/apk/* && \
	\
	./home/teamspeakUpdater.sh "test-only" && \
	rm -rf "${TS_PATH}/"

VOLUME "$TS_PATH"
	
USER "$TS_USER_ID:$TS_GROUP_ID"
	
ENTRYPOINT ["./home/teamspeakUpdater.sh"]