FROM alpine:latest
RUN apk --update add nodejs \
	&& npm install -g todoist-habitrpg \
	&& rm -rf /var/cache/apk/* \
	&& mkdir -p /app \
	&& mkdir -p /app/data
COPY task-sync.sh /app/
RUN chmod +x /app/task-sync.sh
WORKDIR /app
ENTRYPOINT ["/app/task-sync.sh"]
