FROM continuumio/miniconda

# libjpeg from backport, needed for gdal
ADD http://ftp.us.debian.org/debian/pool/main/libj/libjpeg8/libjpeg8_8d-1+deb7u1_amd64.deb /tmp
ADD http://step.esa.int/thirdparties/sen2cor/2.3.1/sen2cor-2.3.1.tar.gz /tmp


RUN conda update conda && \ 
conda install pytables psutil lxml scipy scikit-image && \
dpkg -i /tmp/libjpeg8_8d-1+deb7u1_amd64.deb && \
tar -xzvf /tmp/sen2cor-2.3.1.tar.gz && \
cd /sen2cor-2.3.1 && \
/bin/echo -e "y\ny\ny\n" | python setup.py install 

RUN conda install numpy==1.11.3
# Cleanup
RUN rm -rf /tmp/*

ENV  SEN2COR_HOME=/root/sen2cor SEN2COR_BIN=/opt/conda/lib/python2.7/site-packages/sen2cor-2.3.1-py2.7.egg/sen2cor GDAL_DATA=/opt/conda/lib/python2.7/site-packages/sen2cor-2.3.1-py2.7.egg/sen2cor/cfg/gdal_data
WORKDIR /data
CMD ["L2A_Process"]
