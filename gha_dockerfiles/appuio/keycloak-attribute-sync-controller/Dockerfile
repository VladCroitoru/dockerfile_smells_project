FROM docker.io/library/alpine:3.14

RUN apk add --no-cache curl

WORKDIR /
COPY keycloak-attribute-sync-controller manager
USER 65532:65532

ENTRYPOINT ["/manager"]
