FROM node:8.6.0-alpine

RUN apk add -U --no-cache git openssh-client

LABEL MAINTAINER="fabrice.lecoz@zedesk.net" \
      NODE_VERSION=$NODE_VERSION \
      YARN_VERSION=$YARN_VERSION

USER node
WORKDIR "/app"

ENV PATH /app/.npm-packages/bin:$PATH
RUN echo "prefix=/app/.npm-packages" > ~/.npmrc

VOLUME ["/app","/home/node"]

EXPOSE 8080
EXPOSE 9229
EXPOSE 5858

ENTRYPOINT ["npm"]
CMD ["start"]