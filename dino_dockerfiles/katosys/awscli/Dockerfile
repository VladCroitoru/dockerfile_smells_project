#------------------------------------------------------------------------------
# Set the base image for subsequent instructions:
#------------------------------------------------------------------------------

FROM alpine:3.4
MAINTAINER Marc Villacorta Morera <marc.villacorta@gmail.com>

#------------------------------------------------------------------------------
# Install awscli:
#------------------------------------------------------------------------------

RUN apk add --update groff less python py-pip \
    && pip install --upgrade pip \
    && pip install awscli \
    && apk --purge del py-pip \
    && mkdir -p /aws \
    && rm /var/cache/apk/*

#------------------------------------------------------------------------------
# Entrypoint:
#------------------------------------------------------------------------------

WORKDIR /aws
ENTRYPOINT ["aws"]
