FROM alpine:3.4

# Add runtime dependencies
RUN apk add --no-cache go

# Set up build environment
ENV GOPATH=/usr/local/lib/gocode
ENV LAMPSTAND_SRC_PATH=$GOPATH/src/github.com/nate9/lampstand

COPY . $LAMPSTAND_SRC_PATH
WORKDIR $LAMPSTAND_SRC_PATH

# Build
RUN apk add --no-cache \
    git \
    sqlite \
    gcc musl-dev \
&& ./bootstrap.sh \
&& go build -v \
&& (cd resources; ./setup_tables.sh; mv bible.db ../) \
&& apk del git \
    sqlite \
    gcc musl-dev

# Finalise
EXPOSE 8080

# We want this to execute in shell, therefore we express this in plain
# (not JSON) form
CMD ./lampstand
