# OS
FROM alpine:3.6
LABEL maintainer="nicolas.pulido@crazycake.cl"

# packages
RUN apk update && apk add -U --no-cache --repository=http://dl-4.alpinelinux.org/alpine/edge/testing --allow-untrusted \
	bash \
	python \
	py-pip \
	xvfb \
	dbus \
	fontconfig \
	ttf-freefont \
	wkhtmltopdf \
	&& rm -rf /var/cache/apk/*

# python installs
RUN pip install \
	werkzeug \
	executor \
	gunicorn

# wrapper for xvfb (x11)
COPY wrapper /tmp/
RUN mv /usr/bin/wkhtmltopdf /usr/bin/wkhtmltopdf-origin && \
	mv /tmp/wrapper /usr/bin/wkhtmltopdf && chmod +x /usr/bin/wkhtmltopdf

# set working dir
WORKDIR /root

# copy app
COPY app.py .

# port expose
EXPOSE 80

# entry point
ENTRYPOINT ["/usr/bin/gunicorn"]

# run app
CMD ["-b", "0.0.0.0:80", "--log-file", "-", "app:application"]
