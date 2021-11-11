#FROM lsiobase/alpine.python:3.7
#FROM lsiobase/alpine.python
#FROM lsiobase/python:3.8
FROM lsiobase/alpine.python3

# Set python to use utf-8 rather than ascii.
ENV PYTHONIOENCODING="UTF-8"
ENV UPDATE_FLEXGET="0"                                                                                                                                                                                                             
ENV UPDATE_PIP="0"     

# Copy local files.
COPY etc/ /etc
COPY templates /var/lib/templates
RUN chmod -v +x /etc/cont-init.d/* && apk add gcc python3-dev libc-dev jpeg-dev zlib-dev

# Ports and volumes.
VOLUME /config
WORKDIR /config

EXPOSE 5050
