FROM madnificent/ember:3.26.1 as builder

LABEL maintainer="info@redpencil.io"

WORKDIR /app
COPY package.json .
RUN npm install
COPY . .

RUN ember build -prod

FROM semtech/ember-proxy-service:1.5.1

ENV STATIC_FOLDERS_REGEX "^/(assets|font|tinymce|files)/"

COPY ./proxy/torii-authorization.conf /config/torii-authorization.conf
COPY ./proxy/file-upload.conf /config/file-upload.conf
COPY ./proxy/file-download.conf /config/file-download.conf

COPY --from=builder /app/dist /app
