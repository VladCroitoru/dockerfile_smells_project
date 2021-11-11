# Simple node server that forwards all requests to the same host using HTTPS
#
# Usage: docker run --link=<logging_container>:es_logging_instance -e PORT=<port_number> -e LOGGING_LEVEL=<debug/info/warn/error> --name <container_name> <image_name>
#
# Version 1.1

FROM node:0.12-onbuild
MAINTAINER Wouter Dullaert, wouter.dullaert@gmail.com

# Expose the webserver port
EXPOSE 80

CMD node server.js
