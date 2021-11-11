FROM snazzybucket/idris2api:latest as builder

RUN mkdir /opt/verpackung
WORKDIR /opt/verpackung

COPY . ./
RUN true

RUN make build

FROM ubuntu:20.04

RUN apt-get update && apt-get install --yes nodejs && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /opt/verpackung/exec

COPY --from=builder /opt/verpackung/build/exec /opt/verpackung/exec

ENV PATH="/opt/verpackung/exec:${PATH}"

ENTRYPOINT /opt/verpackung/exec/verpackung
