# gjør det mulig å bytte base-image slik at vi får bygd både innenfor og utenfor NAV
ARG BASE_IMAGE_PREFIX=""
FROM ${BASE_IMAGE_PREFIX}node as node-builder

ADD / /source
ENV CI=true
WORKDIR /source
RUN npm ci && npm run build


FROM ghcr.io/navikt/pus-decorator/pus-decorator:latest
ENV APPLICATION_NAME=arbeidssokerregistrering
COPY --from=node-builder /source/build /app
ADD decorator.yaml /decorator.yaml
ADD decorator-dev-fss.yaml /decorator-dev-fss.yaml
ADD decorator-prod-fss.yaml /decorator-prod-fss.yaml
