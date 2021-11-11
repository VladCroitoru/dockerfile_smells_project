FROM node as builder

ENV NODE_ENV build

WORKDIR /home/app

COPY . /home/app

RUN npm ci \
     && npm run build

FROM node

ENV NODE_ENV production

WORKDIR /home/app

COPY --from=builder /home/app/package*.json /home/app/
COPY --from=builder /home/app/dist/ /home/app/dist/

RUN npm ci

CMD ["npm", "run", "start:prod"]
