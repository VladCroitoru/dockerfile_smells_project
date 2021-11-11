# Docker-Owncloud-client
#
# VERSION               0.9

FROM     alpine
MAINTAINER idef1x <docker@sjomar.eu>

RUN apk update && apk add nextcloud-client bash
ADD startup.sh /startup.sh
RUN chmod +x /startup.sh

# Cleanup

ENTRYPOINT [ "/startup.sh" ]
