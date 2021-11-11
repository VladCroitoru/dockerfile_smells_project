FROM python:2.7.16-stretch
MAINTAINER GeoNode development team

RUN mkdir -p /usr/src/masdap

WORKDIR /usr/src/masdap

# This section is borrowed from the official Django image but adds GDAL and others
RUN apt-get update && apt-get install -y \
		gcc \
		gettext \
		postgresql-client libpq-dev \
		sqlite3 \
                python-gdal python-psycopg2 \
                python-imaging python-lxml \
                python-dev libgdal-dev \
                python-ldap \
                libmemcached-dev libsasl2-dev zlib1g-dev \
                python-pylibmc \
                uwsgi uwsgi-plugin-python \
	--no-install-recommends && rm -rf /var/lib/apt/lists/*


COPY wait-for-databases.sh /usr/bin/wait-for-databases
RUN chmod +x /usr/bin/wait-for-databases

# Upgrade pip
RUN pip install --upgrade pip

# To understand the next section (the need for requirements.txt and setup.py)
# Please read: https://packaging.python.org/requirements/

# fix for known bug in system-wide packages
RUN ln -fs /usr/lib/python2.7/plat-x86_64-linux-gnu/_sysconfigdata*.py /usr/lib/python2.7/

COPY . /usr/src/masdap

RUN pip install --src /usr/src -r requirements.txt

RUN chmod +x /usr/src/masdap/tasks.py \
    && chmod +x /usr/src/masdap/entrypoint.sh

# app-specific requirements
RUN pip install --upgrade -e .

# Install pygdal (after requirements for numpy 1.16)
RUN pip install pygdal==$(gdal-config --version).*

RUN cd /usr/src; git clone https://github.com/GeoNode/geonode-contribs.git -b 2.10.x
RUN cd /usr/src/geonode-contribs/geonode-logstash; pip install -r requirements.txt --upgrade; pip install -e . --upgrade

ENTRYPOINT ["/usr/src/masdap/entrypoint.sh"]
