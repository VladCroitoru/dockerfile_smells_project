FROM alpine:3.5

# install deps, compile, install and remove unnecessary stuff
RUN apk add --update --no-cache git coreutils build-base autoconf automake bash \
                                boost-dev zlib-dev libpng-dev jpeg-dev tiff-dev openexr-dev && \
                                git clone https://github.com/POV-Ray/povray.git && \
                                cd /povray/unix && ./prebuild.sh && \
                                cd /povray && ./configure COMPILED_BY="abousselmi" && make && make install && \
                                apk del build-base autoconf automake && \
                                rm -rf /var/cache/apk/* && \
                                rm -r /povray
