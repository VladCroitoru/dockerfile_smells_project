FROM qnib/nginx

ADD etc/consul-templates/lb.ctmpl /etc/consul-templates/
ADD etc/supervisord.d/lb-update.ini /etc/supervisord.d/
ADD etc/nginx/authorize.lua /etc/nginx/authorize.lua
ADD etc/consul.d/es-lb.json /etc/consul.d/es-lb.json
