FROM node:12.16.1-alpine as builder

WORKDIR /opt/quoting-service

RUN apk add --no-cache -t build-dependencies git make gcc g++ python libtool autoconf automake \
    && cd $(npm root -g)/npm \
    && npm config set unsafe-perm true \
    && npm install -g node-gyp

COPY package.json package-lock.json* /opt/quoting-service/

RUN npm install

RUN apk del build-dependencies

COPY config /opt/quoting-service/config
COPY src /opt/quoting-service/src

FROM node:12.16.1-alpine

WORKDIR /opt/quoting-service

# Create empty log file & link stdout to the application log file
RUN mkdir ./logs && touch ./logs/combined.log
# Links combined to stdout
RUN ln -sf /dev/stdout ./logs/combined.log

# Create a non-root user: ml-user
RUN adduser -D ml-user 
USER ml-user

COPY --chown=ml-user --from=builder /opt/quoting-service .
RUN npm prune --production

EXPOSE 3002
CMD ["npm", "run", "start"]
