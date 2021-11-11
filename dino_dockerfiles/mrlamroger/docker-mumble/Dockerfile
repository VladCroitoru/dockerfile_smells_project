# -----------------------------------------------------------------------------
# docker-mumble
#
# Builds a basic docker image that can run Mumble
# (http://mumble.sourceforge.net/).
#
# Authors: Isaac Bythewood
# Updated: Oct 20th, 2014
# Require: Docker (http://www.docker.io/)
# -----------------------------------------------------------------------------


# Base system is the LTS version of Ubuntu.
from   ubuntu:14.04


# Make sure we don't get notifications we can't answer during building.
env    DEBIAN_FRONTEND noninteractive


# Download and install everything from the repos.
add    ./apt/sources.list /etc/apt/sources.list
run    apt-get --yes update; apt-get --yes upgrade
run    apt-get --yes install mumble-server supervisor pwgen


# Load in all of our config files.
add    ./supervisor/supervisord.conf /etc/supervisor/supervisord.conf
add    ./supervisor/conf.d/murmurd.conf /etc/supervisor/conf.d/murmurd.conf
add    ./mumble/mumble-server.ini /etc/mumble-server.ini
add    ./scripts/start /start


# Fix all permissions
run        chmod +x /start


# 80 is for nginx web, /data contains static files and database /start runs it.
expose 64738
volume ["/data"]
cmd    ["/start"]
