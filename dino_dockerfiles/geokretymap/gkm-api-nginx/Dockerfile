FROM nginx:alpine

# Override those files to match your needs
COPY cors_headers.conf /etc/nginx/
COPY no_cache.conf /etc/nginx/
COPY no_req_limit.conf /etc/nginx/
COPY no_admin_restriction.conf /etc/nginx/
COPY api.geokretymap.org.conf.fastcgi_cache /etc/nginx/
COPY api.geokretymap.org.conf.fastcgi_pass /etc/nginx/
COPY api.geokretymap.org.conf.fastcgi_pass.deny /etc/nginx/


COPY conf.d/ /etc/nginx/conf.d/

