FROM madnificent/ember:3.20.0 as builder

LABEL maintainer="info@redpencil.io"

WORKDIR /app
COPY package.json .
RUN npm install
COPY . .
RUN ember build -prod

FROM semtech/ember-proxy-service:1.5.1
ENV STATIC_FOLDERS_REGEX "^/(assets|font|files|handleiding|@appuniversum)/"
COPY ./proxy/* /config/
COPY --from=builder /app/dist /app
