FROM node:14.16.0 AS builder

WORKDIR /app

COPY src .
COPY package.json .
COPY package-lock.json .
COPY tsconfig.json .
COPY next-env.d.ts .

RUN npm ci --no-fund --no-audit 

RUN npm run build

FROM node:14.16.0 AS application

ENV NODE_ENV=production

WORKDIR /app

COPY --from=builder /app/node_modules node_modules
COPY --from=builder /app/.next .next
COPY ./public ./public
COPY ./src/prisma ./prisma
COPY .env .
COPY entrypoint.sh .
COPY wait.js .

RUN npx prisma generate

CMD ./entrypoint.sh