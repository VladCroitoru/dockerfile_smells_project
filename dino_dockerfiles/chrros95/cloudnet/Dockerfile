# cloudNet, Copyright (C) 2017  Christian Rose
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA
FROM alpine:3.6

ARG BUILD_DATE
ARG VCS_REF
ARG VERSION
ENV NET=cloudNet
LABEL org.label-schema.schema-version="1.0.0-rc.1" \
      org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name="cloudNet" \
      org.label-schema.description="Creating a service to connect different cloud providers and location by vpn" \
      org.label-schema.usage="https://docs.7cb.de/cloudNet/v$VERSION/usage" \
      org.label-schema.url="https:/7cb.de/cloudNet" \
      org.label-schema.vcs-url="https://github.com/chrros95/cloudNet" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vendor="7cb.de" \
      org.label-schema.version=$VERSION
RUN apk update && apk add tinc=1.0.31-r1
ADD healthcheck /healthcheck
RUN chmod +x /healthcheck
VOLUME /etc/tinc
EXPOSE 655
ENTRYPOINT tincd -n $NET -D
HEALTHCHECK CMD /healthcheck