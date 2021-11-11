FROM mhart/alpine-node:16

# Ensure application code makes it into the /app directory
COPY ./ /app/
WORKDIR /app

RUN export NODE_ENV=production && npm ci

# Then we copy over the modules from above onto a `slim` image
FROM mhart/alpine-node:slim-16

EXPOSE 3000

WORKDIR /app
COPY --from=0 /app .

ENTRYPOINT ["./node_modules/pm2/bin/pm2-docker"]
CMD ["start", "index.js", "-i", "max"]
