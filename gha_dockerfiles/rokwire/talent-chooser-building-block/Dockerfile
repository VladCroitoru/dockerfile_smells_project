FROM golang:1.13.14-buster as builder

ENV CGO_ENABLED=0

RUN mkdir /tc-app
WORKDIR /tc-app
# Copy the source from the current directory to the Working Directory inside the container
COPY . .
RUN make

FROM alpine:3.11.6

COPY --from=builder /tc-app/bin/talent-chooser /
COPY --from=builder /tc-app/driver/web/ui /driver/web/ui
COPY --from=builder /tc-app/docs/swagger.yaml /docs/swagger.yaml

COPY --from=builder /etc/passwd /etc/passwd

ENTRYPOINT ["/talent-chooser"]
