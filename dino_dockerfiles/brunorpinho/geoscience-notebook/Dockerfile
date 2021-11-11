# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

FROM jupyter/scipy-notebook:b4dd11e16ae4

USER $NB_USER

RUN conda config --add channels conda-forge

RUN conda install --quiet --yes \
	'geos=3.5*' \
	'gdal=2.1*'

RUN conda install --quiet --yes \
	'shapely=1.5*' \
	'rasterio' \
	'fiona' \
	'geopandas=0.2*' \
	'pyproj=1.9*' \
	'spectral=0.18*' \
	'pythreejs' \
	'folium' \
	'bqplot' \
	'cartopy'

RUN conda install --quiet --yes -p $CONDA_DIR/envs/python2 python=2.7 \
	'geos=3.5*' \
	'gdal=2.1*'

RUN conda install --quiet --yes -p $CONDA_DIR/envs/python2 python=2.7 \
	'shapely=1.5*' \
	'rasterio' \
	'fiona' \
	'geopandas=0.2*' \
	'pyproj=1.9*' \
	'spectral=0.18*' \
	'fatiando=0.5*' \
	'pythreejs' \
	'folium' \
	'bqplot' \
	'cartopy'

RUN conda clean -tipsy

# Install pycpt to use CPT colormaps with matplotlib

RUN pip2 install git+https://github.com/j08lue/pycpt.git
RUN pip3 install git+https://github.com/j08lue/pycpt.git

# Install mplstereonet for stereonet plottting with matplotlib

RUN pip2 install git+https://github.com/joferkington/mplstereonet.git
RUN pip3 install git+https://github.com/joferkington/mplstereonet.git

# Install PyTorch without CUDA

RUN conda install --quiet --yes -c soumith \
	'pytorch' \
	'torchvision' 

RUN conda install --quiet --yes -c soumith -p $CONDA_DIR/envs/python2 python=2.7 \
	'pytorch' \
	'torchvision' 

# Install Mayavi

RUN conda install --quiet --yes -c conda-forge -p $CONDA_DIR/envs/python2 python=2.7 \
	'vtk' \
	'pyqt=4' \
	'mayavi'

RUN conda install --quiet --yes -c conda-forge \
	'vtk' \
	'pyqt=4' \
	'mayavi'

RUN conda clean -tipsy

USER root

# Install a fortran compiler for f2py

RUN apt-get update && \
	apt-get install -y \ 
		gfortran
