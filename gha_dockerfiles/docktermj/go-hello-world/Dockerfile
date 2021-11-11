# -----------------------------------------------------------------------------
# Stages
# -----------------------------------------------------------------------------

ARG IMAGE_GO_BUILDER=golang:1.17.1
ARG IMAGE_FINAL=scratch

# -----------------------------------------------------------------------------
# Stage: go_builder
# -----------------------------------------------------------------------------

FROM ${IMAGE_GO_BUILDER} as go_builder
ENV REFRESHED_AT 2021-10-27
LABEL Name="dockter/hello-world-go-builder" \
      Maintainer="nemo@dockter.com" \
      Version="0.0.5"

# Build arguments.

ARG PROGRAM_NAME="unknown"
ARG BUILD_VERSION=0.0.0
ARG BUILD_ITERATION=0
ARG HELLO_NAME="world"
ARG GO_PACKAGE_NAME="unknown"

# Copy local files from the Git repository.

COPY . ${GOPATH}/src/${GO_PACKAGE_NAME}

# Build go program.

WORKDIR ${GOPATH}/src/${GO_PACKAGE_NAME}
RUN make build-scratch

# --- Test go program ---------------------------------------------------------

# Run unit tests.

# RUN go get github.com/jstemmer/go-junit-report \
#  && mkdir -p /output/go-junit-report \
#  && go test -v ${GO_PACKAGE_NAME}/... | go-junit-report > /output/go-junit-report/test-report.xml

# Copy binaries to /output.

RUN mkdir -p /output \
 && cp -R ${GOPATH}/src/${GO_PACKAGE_NAME}/target/*  /output/

# -----------------------------------------------------------------------------
# Stage: final
# -----------------------------------------------------------------------------

FROM ${IMAGE_FINAL} as final
ENV REFRESHED_AT 2021-10-27
LABEL Name="dockter/hello-world" \
      Maintainer="nemo@dockter.com" \
      Version="0.0.5"

# Copy files from prior step.

COPY --from=go_builder "/output/scratch/go-hello-world" "/"

CMD ["/go-hello-world"]
