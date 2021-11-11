FROM docker.onedata.org/empty-base:1.1.0

COPY gui_static.tar.gz /artefact/

# make artefact available under specfic path for docker < 1.10
RUN ["/bin/busybox","sh","/pub-artefact","/var/www/html"]

