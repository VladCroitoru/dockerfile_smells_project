FROM ubuntu:14.04


# Start installation with some necessary packages
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential \
    git wget curl unzip m4 openssh-client

# install nodejs
RUN curl -sL https://deb.nodesource.com/setup_4.x | sh -
RUN apt-get install -y nodejs
RUN npm install -g bower


# install zlib from source, a dependency for netcdf4-c
RUN wget http://zlib.net/zlib-1.2.8.tar.gz && \
    tar xzfv zlib-1.2.8.tar.gz && cd zlib-1.2.8 && \
    ./configure --prefix=/usr/local && \
    make check && make install && \
    cd .. && rm -rf zlib-1.2.8.tar.gz zlib-1.2.8

# install hdf5 from source, another dependency for netcdf4-c
RUN wget ftp://ftp.unidata.ucar.edu/pub/netcdf/netcdf-4/hdf5-1.8.13.tar.gz && \
    tar xzfv hdf5-1.8.13.tar.gz && cd hdf5-1.8.13 && \
    ./configure --with-zlib=/usr/local --prefix=/usr/local/ --enable-hl --enable-shared && \
    make && make check && make install && make check-install && ldconfig && \
    cd .. && rm -rf hdf5-1.8.13.tar.gz hdf5-1.8.13

# install netcdf4-c
# ref: http://www.unidata.ucar.edu/software/netcdf/docs/getting_and_building_netcdf.html#build_default
#      http://unidata.github.io/netcdf4-python/
RUN wget https://github.com/Unidata/netcdf-c/archive/v4.3.3.1.tar.gz && \
    tar xzfv v4.3.3.1.tar.gz && cd netcdf-c-4.3.3.1 && \
    CPPFLAGS=-I/usr/local/include LDFLAGS=-L/usr/local/lib && \
    ./configure --enable-netcdf-4 --enable-shared --prefix=/usr/local && \
    make check && make install && ldconfig && \
    cd .. && rm -rf v4.3.3.1.tar.gz netcdf-c-4.3.3.1
RUN apt-get install -y python-numpy libncurses5-dev

COPY . /var/www/prms-veg
WORKDIR /var/www/prms-veg
RUN NETCDF4_DIR=/usr/local && HDF5_DIR=/usr/local && pip install -r requirements.txt
ENV PYTHONPATH /var/www/prms-veg

RUN echo '{ "allow_root": true }' > /root/.bowerrc
RUN bower install
RUN git checkout -- app/static/bower_components/swagger-ui/dist/index.html

ENV APP_USERNAME abc@xyz.com
ENV APP_PORT 5000
ENV APP_PASSWORD prms

#CMD gunicorn --worker-class eventlet -w 4 manage:app -b 0.0.0.0:${APP_PORT} \
# --error-logfile='err.log' --access-logfile='log.log' --log-level DEBUG -e \
# APP_USERNAME=${APP_USERNAME} -e APP_PASSWORD=${APP_PASSWORD}

CMD python manage.py runserver -h 0.0.0.0 -p ${APP_PORT} --threaded

#CMD ./serve-swag.sh
