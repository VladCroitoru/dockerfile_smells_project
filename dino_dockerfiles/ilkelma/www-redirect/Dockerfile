FROM nginx:stable

ADD default.conf default.conf 

# Make sure to replace this during runtime!
ENV REDIRECT_HOST=google.com
# In case you want to customize the subdomain (I know it's called www-redirect ;) )
ENV REDIRECT_SUBDOMAIN=www.

CMD envsubst '\$REDIRECT_HOST\ \$REDIRECT_SUBDOMAIN\' < default.conf > /etc/nginx/conf.d/default.conf && nginx -g 'daemon off;'