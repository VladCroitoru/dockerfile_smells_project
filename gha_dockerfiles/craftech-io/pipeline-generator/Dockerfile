FROM python:3.9-alpine3.13

# Python logs to STDOUT
ENV PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

COPY entrypoint.sh /usr/local/bin/entrypoint.sh

# su-exec is installed to prevent the creation of files with python as root user in a local environment
# https://github.com/ncopa/su-exec
RUN apk add --no-cache su-exec \
	&& chmod +x /usr/local/bin/entrypoint.sh

COPY . .

RUN pip install --use-feature=in-tree-build . \
    && rm -rf /app/*

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
