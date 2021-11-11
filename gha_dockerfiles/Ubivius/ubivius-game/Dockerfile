# BUILD_TYPE can have these values: test or prod
# if BUILD_TYPE is empty, set to prod (more secure released image by default)
ARG BUILD_TYPE=prod

FROM ubuntu as build
COPY ./build/Server ./app

FROM ubuntu as test
RUN apt-get update; \
    apt install iproute2 net-tools -y

FROM ubuntu as prod

FROM ${BUILD_TYPE} AS exit_artefact
COPY --from=build /app ./app
EXPOSE 9150/udp
EXPOSE 9151/tcp
CMD ["app/ubivius-server.x86_64"]

