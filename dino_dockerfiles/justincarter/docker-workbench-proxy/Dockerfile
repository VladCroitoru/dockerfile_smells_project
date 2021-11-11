FROM jwilder/nginx-proxy:0.5.0

RUN { \
		echo 'client_max_body_size 100m;'; \
		echo 'proxy_connect_timeout 10m;'; \
		echo 'proxy_send_timeout 10m;'; \
		echo 'proxy_read_timeout 10m;'; \
		echo 'send_timeout 10m;'; \
	} > /etc/nginx/conf.d/workbench-proxy.conf
