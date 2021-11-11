#FROM scratch
FROM debian:jessie
MAINTAINER "Gary Smith" <docker@kc.gs>


#RUN usermod -u 1000 www-data
RUN mkdir -p /storage/app \
	&& mkdir -p /storage/logs \
	&& mkdir -p /storage/framework/cache \
	&& mkdir -p /storage/framework/sessions \
	&& mkdir -p /storage/framework/views \
	&& chown -R www-data /storage \
	&& chmod -R 1777 /storage

# VOLUME ["/storage"]
# WORKDIR /storage
