FROM alpine

RUN apk --no-cache add \
        git \
        bash

ADD changelog.sh /bin/
RUN chmod +x /bin/changelog.sh

ENTRYPOINT /bin/changelog.sh
