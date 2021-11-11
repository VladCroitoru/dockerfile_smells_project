FROM linuxserver/jackett:latest

MAINTAINER LedoKun <romamp100 at gmail dot com>

HEALTHCHECK --interval=5s --timeout=3s CMD curl --fail http://localhost:9117/UI/Dashboard || exit 1
