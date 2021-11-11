FROM docker:18.09.0-ce-tp6 as docker
FROM jenkins:1.651.3-alpine
COPY --from=docker /usr/local/bin/docker /usr/local/bin/docker
