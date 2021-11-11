#
# Minimal service to serve contents from the file system over HTTP.
#
FROM scratch

# Path inside the container to serve files from. Likely will be
# bind mounted from host path or another container at runtime.
ENV FILES_DIR /var/www

COPY ["fileserver", "./"]
COPY ["ca-certificates.crt", "/etc/ssl/certs/"]
CMD ["/fileserver"]
