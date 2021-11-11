FROM x110dc/base
RUN apt-get update && apt-get install -yq apache2-utils nginx && rm /etc/nginx/sites-enabled/default
EXPOSE 80
ENV UPSTREAM_ADDRESS 1.2.3.4
ENV UPSTREAM_PORT 80
ADD proxy.conf /etc/nginx/conf.d/
ADD run.sh /
RUN chmod +x /run.sh
CMD /run.sh
