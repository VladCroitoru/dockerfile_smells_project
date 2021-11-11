 FROM nginx:1.9.9

RUN echo "daemon off;" >> /etc/nginx/nginx.conf

RUN apt-get update
RUN apt-get install -y python supervisor

ADD https://bootstrap.pypa.io/get-pip.py /tmp/get-pip.py
RUN python /tmp/get-pip.py
RUN rm -f /tmp/get-pip.py
RUN pip install python-tutum mako
RUN apt-get clean

COPY conf/ opt/conf/
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY nginx_reload.py /opt/

WORKDIR /opt/


CMD ["supervisord"]