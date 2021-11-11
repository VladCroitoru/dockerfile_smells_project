FROM alpine:3.4

MAINTAINER AlexLee <alexlee7171@gmail.com>

# Install MongoDB
# At the end, remove the apk cache

RUN apk add mongodb --update-cache --repository http://dl-4.alpinelinux.org/alpine/edge/testing --allow-untrusted && \
	rm -rf /var/cache/apk/*

# Create dbdata path
RUN mkdir -p /data/db

# Define mountable directories.
VOLUME ["/data/db"]

# Define default command.
CMD ["mongod"]

EXPOSE 27017