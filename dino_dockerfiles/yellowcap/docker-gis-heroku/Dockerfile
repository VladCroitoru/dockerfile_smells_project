FROM heroku/cedar:14

#### GIS SECTION ####

# Create working directory
RUN mkdir /gissrc
WORKDIR /gissrc

# Create custom bin and lib paths and set env vars
RUN mkdir -p /app/gis/lib
RUN mkdir -p /app/gis/bin
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/app/gis/lib
ENV PATH=$PATH:/app/gis/bin

# CMAKE
RUN curl -s https://cmake.org/files/v3.4/cmake-3.4.3.tar.gz | tar zxv
RUN cd cmake-3.4.3 && ./configure
RUN cd cmake-3.4.3 && make
RUN cd cmake-3.4.3 && make install

# SWIG
RUN curl -s http://netix.dl.sourceforge.net/project/swig/swig/swig-3.0.8/swig-3.0.8.tar.gz | tar zxv
RUN cd swig-3.0.8 && ./configure
RUN cd swig-3.0.8 && make
RUN cd swig-3.0.8 && make install

# PROJ
RUN curl -s http://download.osgeo.org/proj/proj-4.8.0.tar.gz | tar zxv
RUN cd proj-4.8.0 && ./configure --prefix=/app/gis
RUN cd proj-4.8.0 && make
RUN cd proj-4.8.0 && make install

# GEOS
RUN curl -s http://download.osgeo.org/geos/geos-3.5.0.tar.bz2 | tar xvj
RUN cd geos-3.5.0 && ./configure --prefix=/app/gis
RUN cd geos-3.5.0 && make
RUN cd geos-3.5.0 && make install

# GDAL
RUN curl -s http://download.osgeo.org/gdal/2.0.2/gdal-2.0.2.tar.gz | tar zxv
RUN cd gdal-2.0.2 && ./configure --prefix=/app/gis
RUN cd gdal-2.0.2 && make
RUN cd gdal-2.0.2 && make install

# MapServer & MapScript
RUN curl -s http://download.osgeo.org/mapserver/mapserver-7.0.0.tar.gz | tar zxv
RUN mkdir mapserver-7.0.0/build
RUN cd mapserver-7.0.0/build && cmake -DCMAKE_INSTALL_PREFIX=/app/gis -DWITH_PYTHON=ON -DWITH_FRIBIDI=0 -DWITH_FCGI=0 -DWITH_HARFBUZZ=0 -DWITH_GIF=0 .. > ../configure.log
RUN cd mapserver-7.0.0/build && make
RUN cd mapserver-7.0.0/build && make install

#### HEROKU SECTION ####

ENV PORT 3000
WORKDIR /app/user
ENV PATH /app/.heroku/python/bin/:/app/heroku/node/bin/:/app/user/node_modules/.bin:$PATH
RUN mkdir -p /app/.profile.d

#### NODE SECTION ####

# Which version of node?
ENV NODE_ENGINE 0.12.2

# Create some needed directories
RUN mkdir -p /app/heroku/node

# Install node
RUN curl -s https://s3pository.heroku.com/node/v$NODE_ENGINE/node-v$NODE_ENGINE-linux-x64.tar.gz | tar --strip-components=1 -xz -C /app/heroku/node

# Export the node path in .profile.d
RUN echo "export PATH=\"/app/heroku/node/bin:/app/user/node_modules/.bin:\$PATH\"" > /app/.profile.d/nodejs.sh
RUN chmod +x /app/.profile.d/nodejs.sh

#### PYTHON SECTION ####

# Which version of Python?
ENV PYTHON_VERSION python-2.7.11

# Create some needed directories
RUN mkdir -p /app/.heroku/python

# Install Python
RUN curl -s https://lang-python.s3.amazonaws.com/cedar-14/runtimes/$PYTHON_VERSION.tar.gz | tar zx -C /app/.heroku/python

# Install Pip & Setuptools
RUN curl -s https://bootstrap.pypa.io/get-pip.py | /app/.heroku/python/bin/python

# Copy mapscript to python library directory
RUN cp -r /gissrc/mapserver-7.0.0/build/mapscript/python/* /app/.heroku/python/lib/python2.7/

# Install python gdal
RUN cd /gissrc/gdal-2.0.2/swig/python && python setup.py build
RUN cd /gissrc/gdal-2.0.2/swig/python && python setup.py install

# Export the Python environment variables in .profile.d
RUN echo 'export PATH=$HOME/.heroku/python/bin:$PATH PYTHONUNBUFFERED=true PYTHONHOME=/app/.heroku/python LIBRARY_PATH=/app/.heroku/vendor/lib:/app/.heroku/python/lib:$LIBRARY_PATH LD_LIBRARY_PATH=/app/.heroku/vendor/lib:/app/.heroku/python/lib:$LD_LIBRARY_PATH LANG=${LANG:-en_US.UTF-8} PYTHONHASHSEED=${PYTHONHASHSEED:-random} PYTHONPATH=${PYTHONPATH:-/app/user/}' > /app/.profile.d/python.sh
RUN chmod +x /app/.profile.d/python.sh

# Install numpy here to speed up builds
RUN pip install numpy

#### HEROKU SECTION ####

ONBUILD ADD . /app/user/
ONBUILD RUN /app/heroku/node/bin/npm install
ONBUILD RUN /app/.heroku/python/bin/pip install -r requirements.txt

# `init` is kept out of /app so it won't be duplicated on Heroku
# Heroku already has a mechanism for running .profile.d scripts,
# so this is just for local parity
COPY ./init /usr/bin/init

ENTRYPOINT ["/usr/bin/init"]
