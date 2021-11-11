FROM ubuntu:trusty
MAINTAINER Alex Sanz <asans@evirtualpost.com>

ENTRYPOINT ["/app/run-app.sh"]
EXPOSE 25

# Build packages first
COPY deploy/ /app/
RUN /app/provision.sh
