FROM clojure as builder
MAINTAINER Brad Ackerman "brad@facefault.org"

# Download fonts and non-Java programs we need.
# RUN apt-get update && apt-get install -y --no-install-recommends \
#                       pdfjam texlive-latex-recommended \
#  && rm -rf /var/lib/apt/lists/*

# Set up application directory.
ENV APPDIR /docrenderer
RUN mkdir -p "$APPDIR" && chmod -R 775 "$APPDIR"

# Download dependencies.
COPY project.clj "$APPDIR"
WORKDIR "$APPDIR"
RUN lein deps
COPY . "$APPDIR"
RUN mv "$(lein uberjar | sed -n 's/^Created \(.*standalone\.jar\)/\1/p')" \
    app-standalone.jar

FROM alpine:edge
ENV LANG C.UTF-8
MAINTAINER Brad Ackerman "brad@facefault.org"

RUN addgroup -g 31336 docrenderer && adduser -u 31336 -G docrenderer -D docrenderer
RUN apk update && apk upgrade --no-cache && apk add --no-cache texlive openjdk8-jre \
    fontconfig ttf-dejavu ghostscript-fonts \
    && echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> \
        /etc/apk/repositories \
    && apk add --no-cache texmf-dist && rm -rf /var/cache/apk/*

# Set up application directory.
ENV APPDIR /docrenderer
RUN mkdir -p "$APPDIR" && chmod -R 775 "$APPDIR"
COPY --from=builder "${APPDIR}/app-standalone.jar" app-standalone.jar

# Add default locations for config and stylesheets.
ENV STYLESHEETS_DIR="$APPDIR/stylesheets" \
    CONFIG_FILE="$APPDIR/config.toml" \
    FONTS_DIR="/usr/local/share/fonts"
RUN mkdir "$STYLESHEETS_DIR" && chmod 775 "$STYLESHEETS_DIR"
RUN mkdir -p "$FONTS_DIR" && chmod 775 "$FONTS_DIR"
USER docrenderer
CMD ["java", "-jar", "app-standalone.jar"]
EXPOSE 3000
