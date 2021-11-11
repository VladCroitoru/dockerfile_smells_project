FROM alpine:latest

ARG FFAS_TAG=v0.3-alpha
ADD https://github.com/alexellis/faas/releases/download/${FFAS_TAG}/fwatchdog /usr/bin
RUN chmod +x /usr/bin/fwatchdog
CMD ["/usr/bin/watchdog"]
