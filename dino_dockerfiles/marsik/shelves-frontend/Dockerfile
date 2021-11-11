FROM nginx:alpine

COPY nginx.conf /etc/nginx/nginx.conf
RUN mkdir -p /etc/nginx/conf.d
COPY shelves.conf /etc/nginx/conf.d/

# The recommended usage is behind a SSL proxy
EXPOSE 80

# Add and explode the web.war to /web.war directory
RUN apk add --no-cache --virtual .build-deps curl \
 && curl -L -O https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux32 \
 && chmod a+rx jq-linux32 \
 && mkdir -p /web.war \
 && curl -L -s https://api.github.com/repos/MarSik/shelves/releases/latest \
    | ./jq-linux32 --raw-output '.assets[] | .browser_download_url | select(test("web"))' \
    | xargs curl -L -o web-dl.war \
 && unzip -d /web.war web-dl.war \
 && rm -rf /web.war/org /web.war/WEB-INF \
 && apk --no-cache del .build-deps \
 && apk add --no-cache sed \
 && rm -f jq-linux32 web-dl.war

RUN rm -f /etc/nginx/conf.d/default.conf

# Enable API endpoint customization using environment variable
ADD run.sh /bin/
ENTRYPOINT ["/bin/run.sh"]

