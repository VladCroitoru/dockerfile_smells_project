# Secure and Minimal image of Origo
# https://hub.docker.com/repository/docker/huggla/sam-origo

# =========================================================================
# Init
# =========================================================================
# ARGs (can be passed to Build/Final) <BEGIN>
ARG SaM_VERSION="2.0.4"
ARG IMAGETYPE="application"
ARG ORIGO_VERSION="2.4.0"
ARG LIGHTTPD2_VERSION="20201125"
ARG CONTENTIMAGE1="node:alpine"
ARG CONTENTDESTINATION1="/"
ARG BASEIMAGE="huggla/sam-lighttpd2:$LIGHTTPD2_VERSION"
#ARG CLONEGITS="https://github.com/filleg/origo.git -b wfs-qgis"
ARG DOWNLOADS="https://github.com/origo-map/origo/releases/download/v$ORIGO_VERSION/origo-$ORIGO_VERSION.tar.gz"
ARG BUILDDEPS="python2"
ARG BUILDCMDS=\
#"   cd origo "\
" npm install "\
#"&& npm --depth 8 update "\
"&& npm run prebuild-sass "\
"&& npm run build "\
"&& sed -i 's/origo.js/origo.min.js/' build/index.html "\
"&& cp -a build /finalfs/origo"
ARG REMOVEDIRS="/origo/origo-documentation /origo/examples"
# ARGs (can be passed to Build/Final) </END>

# Generic template (don't edit) <BEGIN>
FROM ${CONTENTIMAGE1:-scratch} as content1
FROM ${CONTENTIMAGE2:-scratch} as content2
FROM ${CONTENTIMAGE3:-scratch} as content3
FROM ${CONTENTIMAGE4:-scratch} as content4
FROM ${CONTENTIMAGE5:-scratch} as content5
FROM ${INITIMAGE:-${BASEIMAGE:-huggla/secure_and_minimal:$SaM_VERSION-base}} as init
# Generic template (don't edit) </END>

# =========================================================================
# Build
# =========================================================================
# Generic template (don't edit) <BEGIN>
FROM ${BUILDIMAGE:-huggla/secure_and_minimal:$SaM_VERSION-build} as build
FROM ${BASEIMAGE:-huggla/secure_and_minimal:$SaM_VERSION-base} as final
COPY --from=build /finalfs /
# Generic template (don't edit) </END>

# =========================================================================
# Final
# =========================================================================
ENV VAR_ORIGO_CONFIG_DIR="/etc/origo" \
    VAR_OPERATION_MODE="normal" \
    VAR_setup1_module_load="[ 'mod_deflate' ]" \
    VAR_WWW_DIR="/origo"

# Generic template (don't edit) <BEGIN>
USER starter
ONBUILD USER root
# Generic template (don't edit) </END>
