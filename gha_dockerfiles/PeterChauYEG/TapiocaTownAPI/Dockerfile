FROM node:14.17-alpine As install

WORKDIR /usr/src/app

COPY package*.json .

RUN npm install --only=development

COPY . .

#=====

FROM install as run-local

CMD ["yarn", "start:dev"]

#=====

FROM install as builder

RUN npm run build

#=====

FROM node:14.17-alpine as setup-production

WORKDIR /usr/src/app

COPY package*.json .

RUN npm install --only=production

#COPY --from=builder /usr/src/app/dist ./dist
#COPY --from=builder /usr/src/app/.env .
#COPY --from=builder /usr/src/app/ca-certificate.crt ./dist
#COPY --from=builder /usr/src/app/ca-certificate.crt .
COPY --from=builder /usr/src/app .
EXPOSE 3001
EXPOSE 81

#=====

FROM setup-production as run-production

CMD ["node", "dist/main"]
