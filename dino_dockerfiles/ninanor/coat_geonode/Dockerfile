FROM ubuntu:16.04

RUN apt-get update && apt-get install -y sudo wget

ADD . /root

RUN sudo apt-get update
RUN sudo apt-get install -y python-software-properties software-properties-common
RUN sudo apt-get install -y python-pip git
RUN pip install --upgrade pip

RUN cd /root
RUN git clone -b 2.6.x https://github.com/GeoNode/geonode.git
# install manually because pip can not install binary dependencies
RUN sudo apt-get install -y python-shapely
RUN sudo pip install -e geonode && sudo pip install -r geonode/requirements.txt

# install specific version of Shapely - this might change in the future
RUN sudo pip install --upgrade Shapely==1.5.17

RUN cd geonode && paver setup

# install manually because pip can not install binary dependencies
RUN sudo apt-get install -y python-gdal

# install PostgreSQL
RUN sudo apt-get update
RUN sudo apt-get install -y                 \
        postgresql-9.5                      \
        postgresql-client-9.5               \
        postgresql-contrib-9.5              \
        postgis                             \
        postgresql-9.5-postgis-scripts

# install Java 8
RUN cd /tmp
RUN wget --quiet --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u152-b16/aa0333dd3019491ca4f6ddbe78cdb6d0/jdk-8u152-linux-x64.tar.gz -O jdk.tar.gz
RUN mkdir /opt/jdk
RUN tar -zxf jdk.tar.gz -C /opt/jdk
RUN update-alternatives --install /usr/bin/java java /opt/jdk/jdk1.8.0_152/bin/java 100
RUN update-alternatives --install /usr/bin/javac javac /opt/jdk/jdk1.8.0_152/bin/javac 100

# replace a line in the pg_hba.conf file for PostgreSQL
RUN sudo sh -c "sed -e 's/local   all             all                                     peer/local   all             all                                     trust/' < /etc/postgresql/9.5/main/pg_hba.conf > /etc/postgresql/9.5/main/pg_hba.conf.tmp"
RUN sudo mv /etc/postgresql/9.5/main/pg_hba.conf.tmp /etc/postgresql/9.5/main/pg_hba.conf
RUN echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/9.5/main/pg_hba.conf
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.5/main/postgresql.conf
RUN /etc/init.d/postgresql restart

# create user and databases
RUN /etc/init.d/postgresql start && sleep 30 \
    && sudo -u postgres psql -c "CREATE USER geonode WITH PASSWORD 'geonode'" \
    && sudo -u postgres createdb -O geonode geonode \
    && sudo -u postgres createdb -O geonode geonode_data \
    && sudo -u postgres psql -d geonode_data -c 'CREATE EXTENSION postgis;' \
    && sudo -u postgres psql -d geonode_data -c 'GRANT ALL ON geometry_columns TO PUBLIC;' \
    && sudo -u postgres psql -d geonode_data -c 'GRANT ALL ON spatial_ref_sys TO PUBLIC;'

# migrate COAT
RUN /etc/init.d/postgresql start && cd /root && python manage.py migrate

# create user 'admin'
RUN /etc/init.d/postgresql start && sleep 30 \
    && cd /root && echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'nimda')" | python manage.py shell

# GeoServer port
EXPOSE 8080
# GeoNode port
EXPOSE 8000

# go to /root directory
WORKDIR /root

# start PostgreSQL
ENTRYPOINT /etc/init.d/postgresql start && /bin/bash
