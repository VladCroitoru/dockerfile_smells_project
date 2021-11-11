FROM madnificent/ember:3.6.0 as builder

LABEL maintainer="info@redpencil.io"

WORKDIR /app
COPY package.json .
RUN CYPRESS_INSTALL_BINARY=0 npm install
COPY . .

RUN ember build -prod

FROM semtech/ember-proxy-service:1.4.0

ENV STATIC_FOLDERS_REGEX "^/(assets|fonts|files|ember-pdfjs-wrapper)/"

COPY ./proxy/torii-authorization.conf /config/torii-authorization.conf
COPY ./proxy/file-upload.conf /config/file-upload.conf
COPY ./proxy/chunked-download.conf /config/chunked-download.conf

COPY --from=builder /app/dist /app
