FROM httpd:2.4
# Install tools
RUN apt-get update && \
    apt-get install -y --no-install-recommends unzip curl git ca-certificates && \
    mkdir -p /tmp/downloads
WORKDIR /tmp/downloads

# All environments
ENV PUBLIC_HTML_LOCATION=/usr/local/apache2/htdocs
ENV DOCS_LOCATION=/usr/local/apache2/htdocs/docs

ENV PYTHON_VERSION=3.5.1

# ------------------ Python Docs ------------------
RUN curl -jksSL -o python.zip https://docs.python.org/3/archives/python-${PYTHON_VERSION}-docs-html.zip && \
    unzip -q python.zip && \
    mkdir -p ${DOCS_LOCATION}/python && \
    mv python-${PYTHON_VERSION}-docs-html/* ${DOCS_LOCATION}/python

# ----------------- OpenTSDB Docs -----------------
RUN git clone https://github.com/OpenTSDB/opentsdb.net.git && \
    mkdir -p ${DOCS_LOCATION}/opentsdb && \
    cp -r opentsdb.net/docs/build/html/* ${DOCS_LOCATION}/opentsdb

# Clear all downlaoded and unnecessary files
RUN rm -rf /tmp/downloads && \
  apt-get purge -y unzip curl git ca-certificates && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*

# Copy extra files
COPY ./public_html/ ${PUBLIC_HTML_LOCATION}

RUN chmod 777 -R ${PUBLIC_HTML_LOCATION}
