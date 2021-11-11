FROM alpine:3.7

MAINTAINER Richard Tuin <richard@egeniq.com>

RUN apk add --no-cache curl

# Install Mantra (for scheduled jobs)
RUN curl -o /usr/local/bin/mantra -L https://github.com/pugnascotia/mantra/releases/download/0.0.1/mantra && \
    chmod +x /usr/local/bin/mantra
