FROM debian:jessie

RUN apt-get update && apt-get install -y --no-install-recommends \
		apt-transport-https \
		ca-certificates \
		wget \
        python3-requests \
	&& rm -rf /var/lib/apt/lists/*

RUN wget https://dl.eff.org/certbot-auto \
 && chmod a+x certbot-auto \
 && ./certbot-auto --os-packages-only --non-interactive \
 && rm -rf /var/lib/apt/lists/*

COPY scripts/* /
