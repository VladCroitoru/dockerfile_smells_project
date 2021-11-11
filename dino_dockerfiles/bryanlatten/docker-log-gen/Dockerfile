FROM mhart/alpine-node:12

# Ensure application code makes it into the /app directory
COPY ./ /app/

WORKDIR /app

RUN export NODE_ENV=production && npm ci

EXPOSE 3000

ENTRYPOINT ["./bin/start"]

