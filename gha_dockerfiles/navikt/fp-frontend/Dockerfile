FROM nginxinc/nginx-unprivileged:1.21.3-alpine

LABEL org.opencontainers.image.source=https://github.com/navikt/fp-frontend

ADD proxy.nginx /etc/nginx/conf.d/app.conf.template
ADD start-server.sh /start-server.sh

# FPSAK spesifikk
ENV APP_DIR="/app" \
	APP_PATH_PREFIX="/fpsak" \
	APP_CALLBACK_PATH="/fpsak/cb"

#FPSAK spesifkk
COPY dist /usr/share/nginx/html/fpsak

EXPOSE 9000

# using bash over sh for better signal-handling
CMD sh /start-server.sh
