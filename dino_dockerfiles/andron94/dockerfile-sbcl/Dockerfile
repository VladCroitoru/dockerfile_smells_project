FROM alpine:3.12.0
MAINTAINER Andrii Tymchuk <makedonsky94@gmail.com>

# ================================ Install SBCL ================================

# 1. Testing branch of Alpine edge repository contains latest SBCL version.
ENV ALPINE_EDGE_REPOSITORY http://dl-4.alpinelinux.org/alpine/edge/community

ENV ALPINE_REPOSITORIES /etc/apk/repositories

# 2. Installation:
#  1. Backup Alpine repositories.
#  2. Add Alpine edge repository.
#  3. Update package list.
#  4. Install SBCL.
#  5. Restore Alpine repositories.
#  6. Clean package list.
RUN cp ${ALPINE_REPOSITORIES} ${ALPINE_REPOSITORIES}.backup &&\
    echo ${ALPINE_EDGE_REPOSITORY} >> ${ALPINE_REPOSITORIES} &&\
    apk update &&\
    apk add --no-cache sbcl &&\
    cp ${ALPINE_REPOSITORIES}.backup ${ALPINE_REPOSITORIES} &&\
    rm ${ALPINE_REPOSITORIES}.backup &&\
    rm -fr /var/cache/apk/*

# ==============================================================================

CMD ["sbcl"]
