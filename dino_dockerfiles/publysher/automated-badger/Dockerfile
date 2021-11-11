FROM nginx:alpine
MAINTAINER yigal@publysher.nl

COPY index.html /usr/share/nginx/html

LABEL   org.label-schema.schema-version="1.0" \
        org.label-schema.name="Automated Badger" \
        org.label-schema.description="A simple Proof of Concept on image labels and automated builds" \
        org.label-schema.url="https://github.com/publysher/automated-badger/" \
        org.label-schema.vcs-url="https://github.com/publysher/automated-badger" \
        org.label-schema.vendor="Publysher BV" \
        org.label-schema.docker.dockerfile="./Dockerfile" \
        org.label-schema.docker.cmd.devel="docker run --rm -p 80:80 publysher/automated-badger"
