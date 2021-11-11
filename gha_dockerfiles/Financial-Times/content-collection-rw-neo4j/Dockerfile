FROM golang:1

ENV PROJECT=content-collection-rw-neo4j

ENV ORG_PATH="github.com/Financial-Times"
ENV SRC_FOLDER="${GOPATH}/src/${ORG_PATH}/${PROJECT}"
ENV BUILDINFO_PACKAGE="github.com/Financial-Times/service-status-go/buildinfo."

ARG GITHUB_USERNAME
ARG GITHUB_TOKEN

COPY . ${SRC_FOLDER}
WORKDIR ${SRC_FOLDER}


# Build app
RUN VERSION="version=$(git describe --tag --always 2> /dev/null)" \
  && DATETIME="dateTime=$(date -u +%Y%m%d%H%M%S)" \
  && REPOSITORY="repository=$(git config --get remote.origin.url)" \
  && REVISION="revision=$(git rev-parse HEAD)" \
  && BUILDER="builder=$(go version)" \
  && LDFLAGS="-X '"${BUILDINFO_PACKAGE}$VERSION"' -X '"${BUILDINFO_PACKAGE}$DATETIME"' -X '"${BUILDINFO_PACKAGE}$REPOSITORY"' -X '"${BUILDINFO_PACKAGE}$REVISION"' -X '"${BUILDINFO_PACKAGE}$BUILDER"'" \
  && git config --global url."https://${GITHUB_USERNAME}:${GITHUB_TOKEN}@github.com".insteadOf "https://github.com" \
  && CGO_ENABLED=0 GOPRIVATE=github.com/Financial-Times go build -mod=readonly -a -o /artifacts/${PROJECT} -ldflags="${LDFLAGS}" \
  && echo "Build flags: ${LDFLAGS}"

FROM scratch
WORKDIR /
COPY --from=0 /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
COPY --from=0 /artifacts/* /

CMD [ "/content-collection-rw-neo4j" ]
