#
# Coursera-dl Docker file (https://github.com/coursera-dl/coursera)
#
# Usage and source:
# https://github.com/mshytikov/coursera-dl-docker.git
#

# Pull base image
FROM python:3.6-slim

RUN pip install coursera-dl==0.10.0

VOLUME /downloads

ENTRYPOINT ["coursera-dl", "--path", "/downloads"]
