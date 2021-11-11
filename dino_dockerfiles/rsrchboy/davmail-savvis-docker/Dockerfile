# This software is Copyright (c) 2014 by Chris Weyl <christopher.weyl@savvis.com>
# (That is, effectively by CenturyLinkLabs.)
#
# This work is licensed under a Creative Commons Attribution-ShareAlike 4.0
# International License (CC-BY-SA-4.0).
#
# http://creativecommons.org/licenses/by-sa/4.0/

FROM gimoh/davmail:latest
MAINTAINER Chris Weyl <christopher.weyl@savvis.com>

RUN mkdir /etc/davmail
ADD davmail.properties /etc/davmail/

# add a non-root system user
# note we specify a id so as to *try* to avoid collisions on the host
RUN adduser --system --uid 500 --group --home /var/lib/davmail davmail
RUN chmod 0644 /etc/davmail/*

# ...and use it!
USER davmail

# override default entry point as we've supplied a config
ENTRYPOINT ["/usr/local/davmail/davmail.sh", "/etc/davmail/davmail.properties"]
