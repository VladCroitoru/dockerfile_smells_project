#
# Dockerfile for liquid-feedback
#

FROM debian:buster-slim AS builder

#MAINTAINER Pascal Schneider <https://github.com/DarkGigaByte>

ENV LF_CORE_VERSION v3.2.2
ENV LF_FEND_VERSION v3.2.1
ENV LF_WMCP_VERSION v2.2.0
ENV LF_MOONBRIDGE_VERSION v1.1.1
ENV LF_LATLON_VERSION v0.14

#
# install dependencies
#

RUN apt-get update && apt-get -y remove exim && apt-get -y install \
        build-essential \
        lsb-release\
        postgresql-server-dev-all\
        postgresql\
        msmtp-mta \
        libbsd-dev\
        imagemagick \
        libpq-dev \
        lua5.3 \
        liblua5.3-0 \
        liblua5.3-0-dbg \
        liblua5.3-dev \
        mercurial \
        python-pip \
        pmake \
        curl \
    && pip install markdown2

#
# prepare file tree
#
RUN mkdir -p /opt/lf/sources/patches \
             /opt/lf/sources/scripts \
             /opt/lf/bin

WORKDIR /opt/lf/sources


#
# Download sources
#
RUN hg clone -r ${LF_CORE_VERSION} https://www.public-software-group.org/mercurial/liquid_feedback_core/ ./core \
 && hg clone -r ${LF_FEND_VERSION} https://www.public-software-group.org/mercurial/liquid_feedback_frontend/ ./frontend \
 && hg clone -r ${LF_WMCP_VERSION} https://www.public-software-group.org/mercurial/webmcp ./webmcp\
 && hg clone -r ${LF_MOONBRIDGE_VERSION} https://www.public-software-group.org/mercurial/moonbridge ./moonbridge

#
# Build moonbridge
#
RUN cd /opt/lf/sources/moonbridge\
    && pmake MOONBR_LUA_PATH=/opt/lf/moonbridge/?.lua \
    && mkdir /opt/lf/moonbridge \
    && cp moonbridge /opt/lf/moonbridge/ \
    && cp moonbridge_http.lua /opt/lf/moonbridge/

#
# build core
#
WORKDIR /opt/lf/sources/core

RUN make \
    && cp lf_update lf_update_issue_order lf_update_suggestion_order /opt/lf/bin

#
# build WebMCP
#
WORKDIR /opt/lf/sources/webmcp

RUN make \
    && mkdir /opt/lf/webmcp \
    && cp -RL framework/* /opt/lf/webmcp

WORKDIR /opt/lf/

RUN cd /opt/lf/sources/frontend \
    && hg archive -t files /opt/lf/frontend \
    && cd /opt/lf/frontend/fastpath \
    && make \
    && chown www-data /opt/lf/frontend/tmp


FROM debian:buster-slim

RUN apt-get update && apt-get install --no-install-recommends -y\
                                      msmtp-mta imagemagick python3-pip\
                                      liblua5.3-0 postgresql-client\
 && pip3 install markdown2

COPY --from=builder /opt/lf /opt/lf

#
# setup db
#
RUN cp /opt/lf/sources/core/core.sql /opt/lf/
COPY ./scripts/config_db.sql /opt/lf/

RUN addgroup --system lf \
    && adduser --system --ingroup lf --no-create-home --disabled-password lf


#
# cleanup
#


#
# configure everything
#

# app config (for running container without -v)
COPY ./scripts/lfconfig.lua /opt/lf/frontend/config/
# app config (for copy-if-not-exists when running container with -v)
COPY ./scripts/lfconfig.lua /tmp/

# update script
COPY ./scripts/lf_updated /opt/lf/bin/

# startup script
COPY ./scripts/start.sh /opt/lf/bin/

#
# ready to go
#

EXPOSE 8080

VOLUME /opt/lf/frontend/config/

WORKDIR /opt/lf/frontend

ENTRYPOINT ["/opt/lf/bin/start.sh"]
