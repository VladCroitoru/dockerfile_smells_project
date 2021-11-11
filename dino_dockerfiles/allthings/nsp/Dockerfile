FROM alpine:edge

RUN apk --no-cache add yarn

# Add node user/group with uid/gid 1000:
# This is a workaround for boot2docker issue #581, see
# https://github.com/boot2docker/boot2docker/issues/581
RUN adduser -D -u 1000 node

USER node

ENTRYPOINT ["yarn"]

CMD ["install", "--audit", "--ignore-scripts"]
