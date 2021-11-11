#
# Copyright (C) 2015 Glyptodon LLC
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

#
# Dockerfile for guacamole-client
#

# Start from Tomcat image
FROM tomcat:8.0.20-jre7
MAINTAINER Michael Jumper <mike.jumper@guac-dev.org>

# Version info
ENV \
    GUAC_VERSION=0.9.9      \
    GUAC_JDBC_VERSION=0.9.9 \
    GUAC_LDAP_VERSION=0.9.9 \
    GUAC_NOAUTH_VERSION=0.9.9 \
    GUAC_HMAC_VERSION=1.0.3 \
    GUAC_ENCRYPTEDURL_VERSION=1.0.5

# Add scripts to put core and extensions in place
COPY bin/download* /opt/guacamole/bin/
COPY bin/setup* /opt/guacamole/bin/
COPY guacamole-auth-encryptedurl-$GUAC_ENCRYPTEDURL_VERSION.jar /tmp/

# Download and install latest guacamole-client and authentication
RUN \
    /opt/guacamole/bin/download-guacamole.sh "$GUAC_VERSION" /usr/local/tomcat/webapps && \
    /opt/guacamole/bin/download-jdbc-auth.sh "$GUAC_JDBC_VERSION" /opt/guacamole       && \
    /opt/guacamole/bin/download-ldap-auth.sh "$GUAC_LDAP_VERSION" /opt/guacamole       && \
    /opt/guacamole/bin/download-noauth-auth.sh "$GUAC_NOAUTH_VERSION" /opt/guacamole   && \
    /opt/guacamole/bin/download-hmac-auth.sh "$GUAC_HMAC_VERSION" /opt/guacamole       && \
    /opt/guacamole/bin/setup-encryptedurl-auth.sh "$GUAC_ENCRYPTEDURL_VERSION" /opt/guacamole

# Add the rest of the scripts
COPY bin /opt/guacamole/bin/

# Start Guacamole under Tomcat, listening on 0.0.0.0:8080
EXPOSE 8080
CMD ["/opt/guacamole/bin/start.sh" ]
