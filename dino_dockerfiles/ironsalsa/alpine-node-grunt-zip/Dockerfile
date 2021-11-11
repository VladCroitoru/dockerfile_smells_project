FROM mhart/alpine-node:8
RUN apk --update add zip && rm -rf /var/cache/apk/* && \
    npm install -g grunt-cli && \
    npm install -g karma && \
    npm install -g grunt-karma
CMD [ "/bin/ash" ]
