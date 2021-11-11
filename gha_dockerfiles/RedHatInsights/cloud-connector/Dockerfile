# Use go-toolset as the builder image
# Once built, copy to a smaller image and run from there
FROM registry.redhat.io/ubi8/go-toolset as builder

WORKDIR /go/src/app

COPY go.mod go.sum ./

RUN go mod download

COPY . .

USER root

RUN make build

# Using ubi8-minimal due to its smaller footprint
FROM registry.redhat.io/ubi8/ubi-minimal

WORKDIR /

# Copy executable files from the builder image
COPY --from=builder /go/src/app/cloud-connector /cloud-connector
COPY --from=builder /go/src/app/migrate_db /migrate_db
COPY --from=builder /go/src/app/db/migrations /db/migrations/

USER 1001

EXPOSE 8000 10000
