FROM centos:latest
RUN yum install -y epel-release && \
        yum install -y git bzip2 fontconfig curl wget nodejs redis supervisor && \
	cd /opt && \
	git clone https://github.com/prerender/prerender.git && \
	cd prerender && \
	npm install && \
	npm install prerender-redis-cache prerender-access-log --save && \
	mv server.js server.js.bak && \
	echo 'Prerender successfully installed'
WORKDIR /opt/prerender

VOLUME /var/log/prerender /var/log/redis /var/lib/redis

EXPOSE 3000

# 4 hours
ENV PAGE_TTL=14400
ENV PRERENDER_NUM_WORKERS=4
ENV NUM_SOFT_ITERATIONS=10
ENV PRERENDER_NUM_ITERATIONS=20

ENTRYPOINT ["supervisord", "-c", "/etc/supervisord.conf"]

ADD ./server.js /opt/prerender/server.js
ADD ./supervisord.conf /etc/supervisord.conf
