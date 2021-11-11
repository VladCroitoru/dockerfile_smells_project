# MIT License
# Copyright (c) 2017 Fabian Wenzelmann
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the
# Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

FROM ubuntu:16.04
MAINTAINER Fabian Wenzelmann <fabianwen@posteo.eu>

# whois is required for mkpasswd
RUN apt-get update && apt-get install -y nginx nginx-extras whois

RUN usermod -u 1000 www-data

RUN mkdir /webdav_media
RUN chown -R www-data:www-data /webdav_media

# VOLUME /media
VOLUME /webdav_media
VOLUME /webdav

COPY webdav.conf /default.conf

RUN rm /etc/nginx/sites-enabled/*

COPY entrypoint.sh /
RUN chmod +x entrypoint.sh
COPY webdav_passwd.sh /
RUN chmod +x /webdav_passwd.sh

EXPOSE 80

CMD /entrypoint.sh && nginx -g "daemon off;"
