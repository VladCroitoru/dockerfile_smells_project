FROM node:14-alpine
RUN apk add dumb-init
RUN mkdir /app
WORKDIR /app
COPY package.json /app/package.json
RUN yarn
COPY src /app/src/
COPY lib /app/lib/
COPY test /app/test/
ENTRYPOINT ["/usr/bin/dumb-init", "--"]

# or if you use --rewrite or other cli flags
# ENTRYPOINT ["dumb-init", "--rewrite", "2:3", "--"]

CMD ["yarn", "start"]