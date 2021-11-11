FROM gogs/gogs:latest
MAINTAINER Matt Bentley <mbentley@mbentley.net>

# add existing configuration
ADD data.tar /data

# add sqlite to be able to import db
RUN apk --no-cache add sqlite

# copy in new entrypoint script
COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
