# Start from a Debian image with the latest version of Go installed
# # and a workspace (GOPATH) configured at /go.
FROM golang
#
# # Copy the local package files to the container's workspace.
ADD . /go/src/github.com/waitingkuo/brandkoop-profiler
#
# # Build the outyet command inside the container.
# # (You may fetch or manage dependencies here,
# # either manually or with a tool like "godep".)
#
RUN go get ./... ; exit 0
RUN cd /go/src/github.com/waitingkuo/brandkoop-profiler; go build
RUN cp /go/src/github.com/waitingkuo/brandkoop-profiler/brandkoop-profiler /go/bin/brandkoop-profiler
#
#
# # Run the outyet command by default when the container starts.
ENTRYPOINT /go/bin/brandkoop-profiler
#
# # Document that the service listens on port 8080.
EXPOSE 8080
