##########################
# Build dependencies
##########################
# --platform=$BUILDPLATFORM is used build javascript source with host arch
# Otherwise webpack builds on emulated archs can be extremely slow (+1h)
FROM --platform=${BUILDPLATFORM:-amd64} node:10.19.0-alpine as build

WORKDIR /usr/src/app

RUN apk add --update --no-cache \
    build-base python libpcap-dev linux-headers bash

COPY build/src/package.json ./
COPY build/src/yarn.lock ./
RUN yarn install --production
# Reduces the app dir size from 94.5MB to 71.8MB
RUN npm config set unsafe-perm true
RUN yarn global add modclean && modclean -r



##########################
# Build Typescript app
##########################
FROM build as build-src
RUN yarn install
# Install only --production first to cache them, then install the rest
COPY build/src .
RUN yarn build
# results in /usr/src/app/dist


##########################
# Compute git data
##########################
FROM --platform=${BUILDPLATFORM:-amd64} node:10.19.0-alpine as git-data

WORKDIR /usr/src/app

RUN apk add --no-cache git nodejs
COPY .git .git
COPY dappnode_package.json build/getGitData.js ./
RUN node getGitData /usr/src/app/.git-data.json
# Results in /usr/src/app/.git-data.json


##########################
# Build UI
##########################
FROM --platform=${BUILDPLATFORM:-amd64} node:10.19.0-alpine as build-ui

WORKDIR /usr/src/app

# ensuring both package.json AND package-lock.json are copied
COPY build/ui_openvpn/package*.json ./
COPY build/ui_openvpn/*lock* ./
# install dependencies
RUN yarn install --production
# copy the contents of the app
COPY build/ui_openvpn .
# build for production
ENV REACT_APP_CRED_URL_PATHNAME=/cred \
    REACT_APP_CRED_URL_QUERY_PARAM=id
RUN yarn run build
RUN node injectToHtml build/index.html build/ui_openvpn.html


##########################
# Final stage
##########################
FROM alpine:3.9

WORKDIR /usr/src/app

RUN apk add --update \
    openvpn iptables bash easy-rsa openssl nodejs
RUN ln -s /usr/share/easy-rsa/easyrsa /usr/local/bin && \
    rm -rf /tmp/* /var/tmp/* /var/cache/apk/* /var/cache/distfiles/*

RUN mkdir -p /usr/src/app/secrets

# ENVs used in other ENV statements
ENV OPENVPN=/etc/openvpn \
    DEFAULT_ADMIN_USER=dappnode_admin

# OpenVPN parameters
ENV EASYRSA=/usr/share/easy-rsa \
    EASYRSA_PKI=$OPENVPN/pki \
    EASYRSA_VARS_FILE=$OPENVPN/vars \
    EASYRSA_CRL_DAYS=3650 \
    EASYRSA_BATCH=yes \
    EASYRSA_ALGO=ec \
    EASYRSA_CURVE=prime256v1 \
    # VPN management parameters - OpenVPN params
    DEFAULT_ADMIN_USER=dappnode_admin \
    OPENVPN_CONF=$OPENVPN/openvpn.conf \
    OPENVPN_ADMIN_PROFILE=$OPENVPN/pki/issued/$DEFAULT_ADMIN_USER.crt \
    OPENVPN_CRED_DIR=/usr/www/openvpn/cred \
    OPENVPN_CCD_DIR=$OPENVPN/ccd \
    ON_CLIENT_CONNECT_PATH=/usr/local/bin/ovpn_client_connect \
    # VPN management parameters - Node paths
    INSTALLATION_STATIC_IP=/usr/src/app/config/static_ip \
    SERVER_NAME_PATH=/etc/vpnname \
    GIT_DATA_PATH=/usr/src/app/.git-data.json \
    UI_OPENVPN_PATH=/usr/src/app/ui_openvpn.html \
    # VPN management parameters - URLs
    DYNDNS_HOST=https://ns.dappnode.io \
    DYNDNS_DOMAIN=dyndns.dappnode.io \
    # Used for v2 updates
    CHAP_SECRETS_PATH=/usr/src/app/secrets/chap-secrets \
    # Node
    NODE_ENV=production

RUN mkdir -p ${OPENVPN_CRED_DIR} ${OPENVPN_CCD_DIR}

# No need for webpack, node_modules is 3.3 MB
COPY --from=build /usr/src/app/node_modules /usr/src/app/node_modules
COPY --from=build-src /usr/src/app/dist /usr/src/app/src
COPY --from=build-ui /usr/src/app/build/ui_openvpn.html $UI_OPENVPN_PATH
COPY --from=git-data /usr/src/app/.git-data.json $GIT_DATA_PATH
COPY build/bin /usr/local/bin

VOLUME ["/etc/openvpn"]

EXPOSE 1194/udp

# Prepare external executables
RUN chmod +x /usr/src/app/src/getAdminCredentials.js && \
    chmod +x /usr/src/app/src/vpncli.js && \
    chmod +x /usr/src/app/src/ovpn_client_connect.js && \
    ln -s /usr/src/app/src/getAdminCredentials.js /usr/local/bin/getAdminCredentials && \
    ln -s /usr/src/app/src/vpncli.js /usr/local/bin/vpncli && \
    ln -s /usr/src/app/src/ovpn_client_connect.js $ON_CLIENT_CONNECT_PATH

# Use CMD so it can be replaced when using the VPN image for other calls
CMD ["node", "src/index"]
