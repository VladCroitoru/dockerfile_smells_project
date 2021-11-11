FROM node:14 as BUILD

WORKDIR /usr/src/app
COPY . .

RUN npm ci
RUN npm run build

FROM node:14

ARG COMMIT='unknown'
ENV COMMIT=$COMMIT

WORKDIR /usr/src/app

COPY --from=BUILD /usr/src/app/package*.json ./

RUN npm ci --only=production

HEALTHCHECK --interval=5m --timeout=3s \
  CMD curl -f http://localhost:8300/ || exit 1

COPY --from=BUILD /usr/src/app/dist ./
COPY --from=BUILD /usr/src/app/views ./views/
COPY --from=BUILD /usr/src/app/static ./static/
COPY --from=BUILD /usr/src/app/docs ./docs/

EXPOSE 8300
CMD [ "node", "app.js" ]
