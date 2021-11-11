FROM alpine

RUN apk --update add nodejs git rsync bash && \
	rm -rf /var/cache/apk/* /tmp/* && \
	npm install -g bower && \
	echo '{ "allow_root": true, "analytics": false }' > ~/.bowerrc && \
	mkdir /app

COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

WORKDIR /app

ENTRYPOINT [ "/entrypoint.sh" ]

