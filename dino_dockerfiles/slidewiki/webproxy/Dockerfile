FROM jwilder/nginx-proxy:latest
MAINTAINER Benjamin Wulff (benjamin.wulff.de@ieee.org)

# update nginx.conf so that it includes only conf.d/active.conf 
# and allows larger response body sizes
RUN sed -i 's/include \/etc\/nginx\/conf\.d\/\*\.conf;/include \/etc\/nginx\/conf\.d\/active\.conf;/g' /etc/nginx/nginx.conf && \
    sed -i 's/^http {/&\n    client_max_body_size 50m;/g' /etc/nginx/nginx.conf

# link active.conf -> default.conf
RUN ln -s /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/active.conf

# add script and config for maintenance mode
ADD maintenance /bin/
ADD maintenance.conf /etc/nginx/conf.d/

# add maintenance page content
ADD html /usr/share/nginx/html/maintenance/



