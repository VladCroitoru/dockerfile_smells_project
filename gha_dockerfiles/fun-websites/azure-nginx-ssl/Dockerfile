FROM nginx:1.13

# Install openssh-server to provide web ssh access from kudu, supervisor to run processor
RUN apt-get update \
    && apt-get install --no-install-recommends --no-install-suggests -y   supervisor  openssh-server wget  && echo "root:Docker!" | chpasswd	

# forward request and error logs to docker log collector
RUN mkdir -p /home/LogFiles \
	&& ln -sf /dev/stdout /home/LogFiles/access.log \
	&& ln -sf /dev/stderr /home/LogFiles/error.log

COPY config/nginx.conf /etc/nginx/nginx.conf
COPY config/supervisord.conf /etc/supervisor/conf.d/supervisord.conf	
COPY config/sshd_config /etc/ssh/
COPY app/* /home/site/wwwroot/
COPY app/nasa.gif /home/site/wwwroot/
COPY app/nasa.mp4 /home/site/wwwroot/
RUN mkdir /home/site/wwwroot/embed
COPY app/embed/* /home/site/wwwroot/embed/
COPY scripts/start.sh /bin/
RUN chmod 777 /home/site/wwwroot/index.html -Rf
RUN chmod 777 /home/site/wwwroot/nasa.gif
RUN chmod 777 /home/site/wwwroot/nasa.mp4
RUN chmod 777 /home/site/wwwroot -Rf
RUN chmod 777 /home/site/wwwroot/embed -Rf
EXPOSE 80 443
CMD ["/bin/start.sh"]
