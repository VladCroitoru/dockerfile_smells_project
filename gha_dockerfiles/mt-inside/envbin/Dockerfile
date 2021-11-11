ARG ARCH=
FROM ${ARCH}golang:1.16 as build

WORKDIR /app

COPY go.mod go.sum ./
RUN go mod download

COPY . .
# Because we're building *in* a container for a container, there's no cross-OS-compilation; no need to specify GOOS
# Also because we take ARG ARCH and use buildx (invokes qemu), we always use the native compiler for any platform; never any need to specify GOARCH
RUN go install -a -tags netgo -ldflags "-w $(build/ldflags.sh)" ./cmd/envbin/...
you can do git ops, see - gh-actions-test/.github/workflows/release.yaml
but COPY .git doesn't work, maybe it's somewhere else or something?
Dockerfile should take git info as an ARG, to be provided by
* makefile on local
* another step on GH actions
* -> pass as an arg to ldflags, if not set, try to read locally (ie for native builds)


FROM gcr.io/distroless/base:latest AS run

ARG PORT=8080

COPY --from=build /go/bin/envbin /
COPY *tpl /

EXPOSE $PORT
ENTRYPOINT ["/envbin"]
CMD ["serve"]
