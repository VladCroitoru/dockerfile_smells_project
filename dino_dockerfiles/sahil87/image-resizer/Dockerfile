FROM debian:jessie

RUN apt-get update && \
    apt-get install -y curl supervisor && \
    curl -sL https://deb.nodesource.com/setup_7.x | bash - && apt-get install -y nodejs

#image-resizer vips dependencies
RUN apt-get install -y libgsf-1-dev libvips-dev

COPY . /src

RUN cd /src && \
    npm install -y && \
    node bin/image_resizer.js new -f && \
    npm install -y

ENV PORT 80

WORKDIR /src

EXPOSE 80 443
CMD ["/usr/bin/supervisord", "-n", "-c",  "/src/supervisord.conf"]