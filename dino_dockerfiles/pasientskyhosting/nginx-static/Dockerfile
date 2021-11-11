FROM nginx:1.17

LABEL maintainer "Andreas Krüger <ak@patientsky.com>"

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y -q --install-recommends --no-install-suggests \
        bash \
        openssh-client \
        supervisor \
        php7.3-cli \
        php7.3-curl \
        php7.3-json \
        tzdata \
        curl \
        libjemalloc-dev \
        git && \
    rm -rf /var/lib/apt/lists/* && \
    mkdir -p /var/log/supervisor

ENV LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libjemalloc.so
ADD conf/supervisord.conf /etc/supervisord.conf

# Copy our nginx config
# RUN rm -Rf /etc/nginx/nginx.conf
ADD conf/nginx.conf /etc/nginx/nginx.conf

# nginx site conf
RUN mkdir -p /etc/nginx/sites-available/ && \
    mkdir -p /etc/nginx/sites-enabled/ && \
    mkdir -p /var/www/html/ && \
    touch /etc/nginx/csp.inc.conf

ADD conf/nginx-site.conf /etc/nginx/sites-available/default.conf

RUN ln -s /etc/nginx/sites-available/default.conf /etc/nginx/sites-enabled/default.conf

# Add Scripts
ADD scripts/start.sh /start.sh
RUN chmod 755 /start.sh

# copy in code
ADD errors /var/www/errors/

EXPOSE 80

CMD ["/start.sh"]
