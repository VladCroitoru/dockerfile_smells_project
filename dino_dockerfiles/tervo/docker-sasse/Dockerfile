FROM tensorflow/tensorflow 

RUN mkdir /a
WORKDIR /a
# COPY apt.conf /etc/apt/apt.conf
RUN echo "deb http://ppa.launchpad.net/ubuntugis/ppa/ubuntu xenial main" >> /etc/apt/sources.lits
RUN apt-get update
RUN apt-get --allow-unauthenticated install -y python-tk wget graphviz libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-gdal
RUN pip install matplotlib keras pydot graphviz keras-vis opencv-python psycopg2 unicodecsv SQLAlchemy GeoAlchemy2 pyproj requests xmltodict
