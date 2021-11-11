###############################################################################
#
# In addition to image phusion/baseimage it installs helper script remapuser
# and creates a normal user with uid 1000 and gid 1000 and NO password.
#
# This uid/gid combination maps nicely to the first normal user on most Linux
# systems, so remapping the user via script remapuser shouldn't be necessary
# in the common cases.
#
# IMPORTANT NOTE: user app has NO PASSWORD set!
#
###############################################################################
FROM phusion/baseimage:0.9.17
MAINTAINER Tom Nussbaumer <thomas.nussbaumer@gmx.net>

COPY remapuser /sbin/
RUN addgroup --gid 1000 app && \
adduser --uid 1000 --gid 1000 \
        --disabled-password --gecos "Standard User" app && \
mkdir -p /home/app/.ssh && \
chmod 700 /home/app/.ssh && \
chown app:app /home/app/.ssh

## example how to start up init system and run bash interactive as remapped user app
## (NOTE: we remap to the already set uid/gid ==> does nothing)
CMD ["my_init", "--", "remapuser", "app", "1000", "1000", "/bin/bash", "-li"]
