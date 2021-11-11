FROM mprasil/dokuwiki
MAINTAINER Brendan 'nog3' Halliday <nog3@nog3.net>

# This is a customized docker install of dokuwiki which adds the openauth plugin.

RUN apt-get update && \
    apt-get install -y unzip curl && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# add oauth plugin
RUN curl -O -L "https://github.com/cosmocode/dokuwiki-plugin-oauth/archive/master.zip"
RUN mkdir /dokuwiki/temp
RUN unzip master.zip -d /dokuwiki/temp/
RUN mv /dokuwiki/temp/dokuwiki-plugin-oauth-master/ /dokuwiki/lib/plugins/oauth
RUN rm -rf master.zip
