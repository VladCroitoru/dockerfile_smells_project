FROM docker:dind

ARG S6_VER="1.22.1.0"
ARG NODEBOOK_VER="0.2.0"

RUN mkdir /_install


# Update this to 2 Step unzip @ ubuntu 20.04
ADD https://github.com/just-containers/s6-overlay/releases/download/v${S6_VER}/s6-overlay-amd64.tar.gz /_install
RUN gunzip -c /_install/s6-overlay-amd64.tar.gz | tar -xf - -C / && \
    mkdir -p /app /notebooks
ENTRYPOINT ["/init"]


ADD https://github.com/netgusto/nodebook/releases/download/${NODEBOOK_VER}/nodebook-linux /app/
RUN chmod +x /app/nodebook-linux


COPY docker/root /


EXPOSE 80
WORKDIR /notebooks
VOLUME /var/lib/docker /notebooks


RUN rm -r /_install
