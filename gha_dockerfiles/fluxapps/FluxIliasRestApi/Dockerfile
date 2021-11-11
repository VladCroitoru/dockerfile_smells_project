FROM alpine:latest AS build

COPY --from=docker-registry.fluxpublisher.ch/flux-rest/api:latest /FluxRestApi /FluxIliasRestApi/libs/FluxRestApi
COPY . /FluxIliasRestApi

FROM scratch

LABEL org.opencontainers.image.source="https://github.com/fluxapps/FluxIliasRestApi"
LABEL maintainer="fluxlabs <support@fluxlabs.ch> (https://fluxlabs.ch)"

COPY --from=build /FluxIliasRestApi /FluxIliasRestApi
