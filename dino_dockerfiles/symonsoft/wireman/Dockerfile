FROM nginx:1.13.0

# Copy bootstrap configuration files
COPY nginx.conf /bootstrap/nginx.conf
COPY bootstrap.sh /bootstrap/bootstrap.sh

# Bootstrap command
ENTRYPOINT ["/bootstrap/bootstrap.sh"]
