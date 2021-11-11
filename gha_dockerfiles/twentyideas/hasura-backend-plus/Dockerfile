FROM node:14-alpine AS builder
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm install
COPY . .
RUN npm run build

FROM node:14-alpine
ARG NODE_ENV=production
ENV NODE_ENV $NODE_ENV
ENV PORT 3000

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm install

COPY --from=builder /app/dist/ dist/
COPY custom custom
COPY metadata metadata
COPY migrations migrations
COPY migrations-v1 migrations-v1

HEALTHCHECK --interval=60s --timeout=2s --retries=3 CMD wget localhost:${PORT}/healthz -q -O - > /dev/null 2>&1

EXPOSE $PORT
CMD ["npm", "run", "start"]
