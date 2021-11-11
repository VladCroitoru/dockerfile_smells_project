FROM python:3.5-jessie
MAINTAINER mnementh64 s.caillet@free.fr

ENV UID 1000
ENV GID 1000

# Install mkdocs
RUN pip install mkdocs
RUN pip install mkdocs-material

RUN useradd -m mkdocuser

RUN mkdir /mkdoc
WORKDIR /mkdocs

COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["bash", "/entrypoint.sh"]
