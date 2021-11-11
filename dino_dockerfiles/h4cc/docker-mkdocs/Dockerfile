FROM alpine:3.5
MAINTAINER Julius Beckmann <h4cc@github.com>

# Install python2 and newest pip
RUN apk add --update py2-pip && pip install --upgrade pip && rm -rf /var/cache/apk/*

# Install MkDocs
RUN pip install -I mkdocs==0.16.1 \
	mkdocs-inspired mkdocs-material mkdocs-cinder mkdocs-pandoc mkdocs-psinder \
	mkdocs-alabaster mkdocs-basic-theme mkdocs-boost mkdocs-bootstrap \
	mkdocs-cluster mkdocs-jinks mkdocs-juice \
	mkdocs_autodoc mkdocs_tree && rm -rf /tmp/*

# Define dirs
VOLUME ["/mkdocs"]
WORKDIR "/mkdocs"

# Expose default serve port.
EXPOSE 8000

ENTRYPOINT ["mkdocs"]
