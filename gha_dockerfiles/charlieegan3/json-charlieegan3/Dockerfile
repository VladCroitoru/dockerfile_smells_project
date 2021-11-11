FROM golang:1.10 as build

WORKDIR /go/src/github.com/charlieegan3/json-charlieegan3

COPY . .

RUN CGO_ENABLED=0 go build -o statusUpdater cmd/run.go


FROM scratch
ADD ca-certificates.crt /etc/ssl/certs/
COPY --from=build /go/src/github.com/charlieegan3/json-charlieegan3/statusUpdater /
CMD ["/statusUpdater"]
