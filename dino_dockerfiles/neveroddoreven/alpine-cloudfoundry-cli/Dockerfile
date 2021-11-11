FROM alpine:3.7

# Useful behind corporate proxy w/ cert mangling
ARG CACERT_VAL

ENV CF_DIAL_TIMEOUT 120

ADD scripts /scripts

RUN apk add --no-cache ca-certificates bash make git curl
# Suppress output to a logfile (it emits an unnecessary warning)

RUN [ -n "${CACERT_VAL}" ] \
    && /scripts/utility.cli.sh -s "${CACERT_VAL}" -o /usr/local/share/ca-certificates/CACERT_VAL.crt install-cacert \
    || echo "CACERT_VAL skipped"

RUN update-ca-certificates 2>/dev/null

RUN ls -lrt /etc/ssl/certs | find /etc/ssl/certs -name *CACERT* 

RUN curl -L "https://cli.run.pivotal.io/stable?release=linux64-binary&source=github&version=6.36.1"  | tar -zx -C /usr/local/bin

