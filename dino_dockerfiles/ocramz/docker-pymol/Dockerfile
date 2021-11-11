#################################################################
# Dockerfile
#
# Version:          1
# Software:         PyMol
# Software Version: 1.8.2.0
# Description:      protein visualization
# Website:          
# Tags:             Visualization
# Provides:         PyMol 1.8.2.0
# Base Image:       ubuntu 14.04
# Build Cmd:        
# Pull Cmd:         
# Run Cmd:          
#################################################################

FROM ubuntu:14.04
MAINTAINER Marco Zocca, zocca.marco gmail 


# # # environment variables
ENV PYMOL_VERSION 1.8.2.0
ENV PYMS_DIR /home/scripts/PyMol
ENV DATASETS_DIR /home/datasets
ENV IPYNBS_DIR /home/scripts/iPython

# # useful directories
RUN mkdir -p ${PYMS_DIR}
RUN mkdir -p ${DATASETS_DIR}
RUN mkdir -p ${IPYNBS_DIR}

# # scripts and datasets (FIXME: better use VOLUME instead, see Dockerfile docs)

ADD scripts/ ${PYMS_DIR}
ADD datasets/ ${DATASETS_DIR}
ADD ipymol/ ${IPYNBS_DIR}



RUN apt-get update 

# # # bash
RUN rm /bin/sh && ln -s /bin/bash /bin/sh


# # # install some build tools
RUN apt-get install -y sudo wget curl make python python-pip pkg-config


# # # install PyMol, iPython, iPyMol +  dependencies (separated by double space)
RUN apt-get install -y freeglut3 freeglut3-dev libpng3 libpng-dev libfreetype6 libfreetype6-dev pmw python-dev glew-utils libglew-dev libxml2-dev    libatlas-base-dev libgsl0-dev libblas-dev liblapack-dev gfortran libzmq1 libzmq-dev libc-dev   libtiff4-dev libjpeg8-dev zlib1g-dev liblcms2-dev libwebp-dev tcl8.5-dev tk8.5-dev python-tk


# # # for reference : CVXOPT dependencies (scipy and numpy)
# # # sudo apt-get install python3-numpy python3-scipy liblapack-dev libatlas-base-dev libgsl0-dev fftw-dev libglpk-dev libdsdp-dev



# # # # iPython + iPyMol + dependencies
RUN pip install pyzmq ipython jupyter jinja2 tornado numpy  scipy  ipymol matplotlib freetype-py






# # # # # Python virtualenv
# # RUN pip install virtualenv
# # RUN pip install virtualenvwrapper
# # # RUN source /usr/local/share/python/virtualenvwrapper.sh
# # # RUN mkvirtualenv venv







# # # clean temp data
RUN apt-get clean && apt-get purge && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*












# # # fetch and install PyMOl

RUN wget --no-verbose https://sourceforge.net/projects/pymol/files/pymol/1.8/pymol-v${PYMOL_VERSION}.tar.bz2
RUN tar jxf pymol-v${PYMOL_VERSION}.tar.bz2
RUN rm pymol-v*
WORKDIR pymol
RUN python setup.py build install


# # # set working dir 
# WORKDIR /home

# # # start Python in interactive mode and load PyMol without a GUI
# ENTRYPOINT ["python", "-ic", "execfile('pymol_scripts/pymol_init.py')"]






# # # # iPyMol : control PyMol via Jupyter/iPython

# # # example usage of iPyMol
# # from ipymol import viewer as pymol
# # pymol.start()   # Start PyMOL RPC server
# # pymol.do('fetch 3odu; as cartoon; bg white')
# # pymol.show()






# # # iPython-related

# VOLUME /notebooks
# WORKDIR /notebooks

# # for converting notebooks...
# RUN pip install pygments
# RUN apt-get install -y pandoc



EXPOSE 8888
ENTRYPOINT jupyter notebook --NotebookApp.port=8888 '--NotebookApp.ip=*' # --NotebookApp.notebook_dir=/notebooks

# # # Usage:
# # docker run -p 8888:8888 -v `/bin/pwd`:/notebooks  -t ocramz/docker-pymol




# # # free space on the image

RUN apt-get remove -y --purge libzmq-dev python-dev libc-dev; \
     apt-get remove -y --purge gcc cpp binutils; \
     apt-get autoremove -y; \
     apt-get clean -y