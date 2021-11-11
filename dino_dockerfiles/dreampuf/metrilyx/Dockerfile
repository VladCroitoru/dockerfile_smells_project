FROM ubuntu

RUN apt-get -y update \
 && apt-get install -y curl wget make gfortran libuuid1 uuid-runtime python-setuptools python-dev libpython-dev git-core libffi-dev libatlas-dev libblas-dev python-numpy nginx
RUN curl -s http://metrilyx.github.io/bootstrap.sh  | bash -s -- install
RUN pip install git+https://github.com/Ticketmaster/metrilyx-2.0.git
RUN cp /opt/metrilyx/etc/metrilyx/metrilyx.conf.sample /opt/metrilyx/etc/metrilyx/metrilyx.conf \
 && cp /opt/metrilyx/data/metrilyx.sqlite3.default /opt/metrilyx/data/metrilyx.sqlite3 \
 && sed -i -e "s/<OpenTSDB host>/OPENTSDB/g" /opt/metrilyx/etc/metrilyx/metrilyx.conf \
 && rm /etc/nginx/sites-enabled/default \
 && sed -i "s/user .\+;/user www-data;/g" /etc/nginx/nginx.conf \
 && chown -R www-data:www-data /opt/metrilyx \
 && sed -i "s/NGINX_USER=.\+/NGINX_USER=\"www-data\"/g" /etc/init.d/metrilyx \
 && sed -i -e "s/uid.\+/uid\t\t= www-data/g" -e "s/gid.\+/gid\t\t= www-data/g" /opt/metrilyx/etc/metrilyx/uwsgi.conf


EXPOSE 80
ADD start.sh /opt/metrilyx/
RUN chmod 0744 /opt/metrilyx/start.sh
CMD ["/bin/bash", "/opt/metrilyx/start.sh"]
