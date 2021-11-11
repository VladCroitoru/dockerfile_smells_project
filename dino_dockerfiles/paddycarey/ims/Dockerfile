FROM gliderlabs/alpine:latest

COPY . /src
RUN cd /src && ./build.sh "$(cat VERSION)"

WORKDIR /mnt/images
VOLUME /mnt/images
EXPOSE 5995

ENTRYPOINT ["/bin/ims"]
