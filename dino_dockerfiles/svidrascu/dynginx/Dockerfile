FROM nginx:stable

MAINTAINER Sergiu Vidrascu vsergiu@hotmail.com

COPY nginx* /etc/nginx/
RUN ["chmod", "+x", "/etc/nginx/nginxstart.sh"]

ENTRYPOINT ["/etc/nginx/nginxstart.sh"]
