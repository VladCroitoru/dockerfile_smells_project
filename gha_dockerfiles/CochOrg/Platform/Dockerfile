# Copyright 2015 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Dockerfile for PHP 8.0 using nginx as the webserver.
FROM gcr.io/platform-322711/php:latest

ENV DOCUMENT_ROOT /app/public

RUN cd storage/ \
    && mkdir -p framework/{session,views,cache} \
    && chmod -R 775 framework \
    && chown -R www-data:www-data framework

COPY .htpasswd /etc/nginx/conf.d/

RUN composer update

RUN apt-get update && apt-get install -y ca-certificates curl

ARG NODE_VERSION=16.9.1
ARG NODE_PACKAGE=node-v$NODE_VERSION-linux-x64
ARG NODE_HOME=/opt/$NODE_PACKAGE
ENV NODE_PATH $NODE_HOME/lib/node_modules
ENV PATH $NODE_HOME/bin:$PATH
RUN curl https://nodejs.org/dist/v$NODE_VERSION/$NODE_PACKAGE.tar.gz | tar -xzC /opt/

RUN cd /app \
    ln -s /app/storage/app/public /app/public/storage \
    && npm install \
    && php artisan optimize:clear \
    && npm run dev
#    && chmod -R 775 $DOCUMENT_ROOT \
#    && chown -R www-data:www-data $DOCUMENT_ROOT \
#    && ls -l

