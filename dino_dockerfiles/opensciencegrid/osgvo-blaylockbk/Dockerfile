FROM opensciencegrid/osgvo-el7

RUN yum -y upgrade

RUN yum -y install \
           geos \
           geos-devel \
           geos-python \
           grib_api \
           grib_api-devel \
           hdf5 \
           hdf5-devel \
           netcdf \
           netcdf-devel \
           netcdf4-python \
           proj \
           proj-devel \
           python-pip \
           wgrib \
           wgrib2

RUN pip install --upgrade pip

# pyproj and pygrib
RUN pip install --upgrade numpy
RUN pip install --upgrade pyproj
RUN pip install --upgrade matplotlib
RUN pip install --upgrade https://github.com/matplotlib/basemap/archive/v1.1.0.tar.gz
RUN pip install --upgrade pygrib

# build info
RUN echo "Timestamp:" `date --utc` | tee /image-build-info.txt

