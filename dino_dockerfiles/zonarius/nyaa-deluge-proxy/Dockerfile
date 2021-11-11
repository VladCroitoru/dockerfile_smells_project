FROM node:10-alpine

ENV NODE_ENV=production

# Needed for NPM install
RUN apk --no-cache add git

COPY "." "/app"

# Build express server & frontend
RUN cd /app && \
    npm ci && \
    cd /app/react-frontend && \
    npm ci && \
    npm run build && \
    rm -rf node_modules && \
    apk del git

WORKDIR /app
EXPOSE 8080

ENTRYPOINT [ "node", "src/app.js" ]
