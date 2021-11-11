#
# see https://github.com/nginxinc/docker-nginx
#
FROM jwilder/nginx-proxy

RUN apt-get update \
 && apt-get upgrade -y -o Dpkg::Options::="--force-confnew" --no-install-recommends \
 && apt-get autoremove \
 && apt-get clean -y \
 && rm -rf /tmp/* \
 && rm -rf /var/tmp/* \
 && for logs in `find /var/log -type f`; do > $logs; done \
 && rm -rf /usr/share/locale/* \
 && rm -rf /usr/share/man/* \
 && rm -rf /usr/share/doc/* \
 && rm -rf /var/lib/apt/lists/* \
 && rm -f /var/cache/apt/*.bin

RUN { \
      echo 'client_max_body_size 100m;'; \
    } > /etc/nginx/conf.d/my_proxy.conf
