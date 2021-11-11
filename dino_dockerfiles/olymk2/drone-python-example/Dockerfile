# Docker image for the Drone build runner
#
#     CGO_ENABLED=0 go build -a -tags netgo
#     docker build --rm=true -t plugins/drone-cache .

FROM python
COPY ./example.py /bin/example
ENTRYPOINT ["/bin/example"]
