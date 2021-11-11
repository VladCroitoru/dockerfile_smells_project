FROM node:14-alpine
ENV PORT=3000
WORKDIR /app
EXPOSE 3000
COPY . ./
RUN yarn
CMD [ "yarn", "run", "start" ]

HEALTHCHECK --interval=15s \
  --timeout=10s \
  --start-period=30s \
  --retries=3 \
  CMD [ "/usr/bin/wget", "--tries=1", "--spider", "localhost:3000" ]
