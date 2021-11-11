FROM madnificent/ember:3.16.0 as builder

LABEL maintainer="info@redpencil.io"

WORKDIR /app
COPY package.json .
RUN npm install
COPY . .
RUN EMBER_TEST_SELECTORS_STRIP=false ember build -prod
RUN git clone https://github.com/lblod/handleiding-digitaal-loket.git handleiding \
      && rm -r handleiding/.git \
      && mv handleiding /app/dist/handleiding

FROM semtech/ember-proxy-service:1.4.0

ENV STATIC_FOLDERS_REGEX "^/(assets|font|files|handleiding|toezicht/bestanden|@appuniversum)/"

COPY ./proxy/torii-authorization.conf /config/torii-authorization.conf
COPY ./proxy/file-upload.conf /config/file-upload.conf

COPY --from=builder /app/dist /app
