#    Python with Firefox and Xvfb Dockerfile.
#    Copyright (c) 2015, 2016, 2017 Richard Huang <rickypc@users.noreply.github.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

FROM alpine:latest
MAINTAINER Richard Huang <rickypc@users.noreply.github.com>

RUN apk add --no-cache bash curl dbus firefox-esr fontconfig python ttf-freefont xvfb

# Prevent time drift
RUN ntpd -dqnp pool.ntp.org

# Add gecko driver
ARG GECKODRIVER_VERSION=0.15.0
ARG GECKODRIVER_FILE=v${GECKODRIVER_VERSION}/geckodriver-v${GECKODRIVER_VERSION}-linux64.tar.gz
RUN curl -s -o /tmp/geckodriver.tar.gz -L \
  https://github.com/mozilla/geckodriver/releases/download/$GECKODRIVER_FILE \
  && rm -rf /usr/bin/geckodriver \
  && tar -C /usr/bin -zxf /tmp/geckodriver.tar.gz \
  && rm /tmp/geckodriver.tar.gz \
  && mv /usr/bin/geckodriver /usr/bin/geckodriver-$GECKODRIVER_VERSION \
  && chmod 755 /usr/bin/geckodriver-$GECKODRIVER_VERSION \
  && ln -fs /usr/bin/geckodriver-$GECKODRIVER_VERSION /usr/bin/geckodriver
