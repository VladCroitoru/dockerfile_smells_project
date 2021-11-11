From alpine

RUN apk update && apk upgrade && apk --no-cache -U add openrc curl tcpdump tcptraceroute lsof iperf nmap nginx && rm -f /etc/nginx/conf.d/default.conf && echo 1 > /var/lib/nginx/html/index.html && rc-update add nginx

ADD default.conf /etc/nginx/conf.d/default.conf

ONBUILD RUN apk update && apk upgrade

EXPOSE 11111
