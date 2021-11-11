# Copyright (c) 2021 Target Brands, Inc. All rights reserved.
#
# Use of this source code is governed by the LICENSE file in this repository.

##############################################################################
##    docker build --no-cache --target certs -t secret-vault:certs .    ##
##############################################################################

FROM alpine as certs

RUN apk add --update --no-cache ca-certificates

###############################################################
##      docker build --no-cache -t secret-vault:local .      ##
###############################################################

FROM alpine:latest

COPY --from=certs /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/ca-certificates.crt

COPY release/secret-vault /bin/secret-vault

ENTRYPOINT ["/bin/secret-vault"]