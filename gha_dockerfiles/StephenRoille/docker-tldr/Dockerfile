FROM python:alpine

LABEL "org.opencontainers.image.authors"="Stephen Roille"
LABEL "org.opencontainers.image.url"="https://hub.docker.com/r/stephenroille/tldr"
LABEL "org.opencontainers.image.source"="https://github.com/StephenRoille/docker-tldr"
LABEL "org.opencontainers.image.licenses"="GPL-3.0-or-later"
LABEL "org.opencontainers.image.title"="tldr Python client"
LABEL "org.opencontainers.image.description"="Dockerize the tldr Python client, the man pages for fulfilled developers"
LABEL "org.opencontainers.image.base.name"="docker.io/library/python:alpine"


RUN apk update
RUN pip3 install --no-cache tldr

# https://github.com/tldr-pages/tldr-python-client#usage
ENV TLDR_COLOR_NAME="red"
ENV TLDR_COLOR_DESCRIPTION="white"
ENV TLDR_COLOR_EXAMPLE="cyan"
ENV TLDR_COLOR_COMMAND="magenta"
ENV TLDR_COLOR_PARAMETER="white"
ENV TLDR_LANGUAGE="en"
ENV TLDR_CACHE_ENABLED=1
ENV TLDR_CACHE_MAX_AGE=720
ENV TLDR_PAGES_SOURCE_LOCATION="https://raw.githubusercontent.com/tldr-pages/tldr/master/pages"
ENV TLDR_DOWNLOAD_CACHE_LOCATION="https://tldr-pages.github.io/assets/tldr.zip"

ENTRYPOINT [ "tldr" ]
CMD ["--help"]
