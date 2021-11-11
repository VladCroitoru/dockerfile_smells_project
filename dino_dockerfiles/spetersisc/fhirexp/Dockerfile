FROM alpine:3.6

RUN apk update \
 && apk upgrade \
 && apk add --no-cache bash supervisor curl git libc6-compat nginx nodejs nodejs-npm libgit2-dev build-base \
 && rm -rf /var/cache/apk/* \

# INSTALL `ORION` USING `NPM`
#
# Parameters:
#
# (-) BUILD_ONLY=true: https://github.com/nodegit/nodegit/issues/1039#issuecomment-223516656
# (-) --production:    https://wiki.eclipse.org/Orion/Node/Getting_started#Installing_with_npm
# (-) --unsafe-perm:   https://github.com/nodejs/node-gyp/issues/454#issuecomment-134140378

 && BUILD_ONLY=true npm install --production --unsafe-perm -g orion \
 && apk del libgit2-dev build-base \

 && mkdir /gotty \
 && cd /gotty \
 && curl -LO https://github.com/yudai/gotty/releases/download/v1.0.1/gotty_linux_amd64.tar.gz \
 && tar -xzf gotty_linux_amd64.tar.gz \
 && rm gotty_linux_amd64.tar.gz \

 && rm -rf /tmp/*

# Nginx tweaks:
#
# (-) fix the nginx .pid bug (https://github.com/gliderlabs/docker-alpine/issues/185#issuecomment-246595114)
# (-) remove the default site
# (-) tweak nginx config to log errors to stderr (with increased verbosity)
# (-) tweak nginx config to log  access logs to stdout

RUN mkdir -p /run/nginx \
 && rm /etc/nginx/conf.d/default.conf \
 && sed -i 's:/var/log/nginx/error.log warn:stderr notice:g' /etc/nginx/nginx.conf \
 && sed -i 's:/var/log/nginx/access.log:/dev/stdout:g' /etc/nginx/nginx.conf \

# Set bash prompt to show the current directory and add some useful aliases:

 && echo 'PS1="\w# "' >> /root/.bashrc \
 && echo 'alias ll="ls -l"' >> /root/.bashrc \
 && echo 'alias la="ls -la"' >> /root/.bashrc


RUN mkdir -p /usr/cachesys/Data
ADD supervisord.conf /etc/
ADD nginx-orion-gotty.conf /etc/nginx/conf.d/
ADD entry.html /var/lib/nginx/html/
ADD fhir.html /var/lib/nginx/html/
RUN mkdir -p /var/lib/nginx/html/isc-images
COPY isc-images/* /var/lib/nginx/html/isc-images/
EXPOSE 8888

CMD ["supervisord"]
