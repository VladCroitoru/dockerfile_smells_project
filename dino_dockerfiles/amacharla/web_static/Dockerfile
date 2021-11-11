FROM nginx

MAINTAINER Anoop Macharla <149@holbertonschool.com>

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
	&& ln -sf /dev/stderr /var/log/nginx/error.log

# tell the container what port will be using 
EXPOSE 80

# Move respective files to right location based on configration
COPY static /usr/share/nginx/html
COPY nginx_site.template /etc/nginx/conf.d/nginx_site.template

# Remove default configuration from Nginx and add custom
RUN ln -fs /etc/nginx/conf.d/nginx_site.template /etc/nginx/conf.d/default.conf 

# Make NGINX run on the foreground
CMD ["nginx", "-g", "daemon off;"]
