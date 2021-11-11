# Name: korniichuk/jupyterhub
# Short Description: JupyterHub
# Full Description: The jupyter/notebook Docker image with JupyterHub.
# Version: 0.1a1

FROM jupyter/notebook

MAINTAINER Ruslan Korniichuk <ruslan.korniichuk@gmail.com>

USER root

# Retrieve new lists of packages
ENV REFRESHED_PACKAGES_AT 2016–01–10
RUN apt-get -qq update # -qq -- no output except for errors

# Install nodejs, nodejs-legacy
RUN apt-get install -y nodejs nodejs-legacy && apt-get clean

# Install npm for configurable-http-proxy installation
RUN apt-get install -y npm && apt-get clean

# Install configurable-http-proxy
RUN npm install -g configurable-http-proxy

# Install pip3 for jupyterhub installation
RUN apt-get install -y python3-pip && apt-get clean

# Install jupyterhub
RUN pip3 install jupyterhub

# Install IPython Notebook
RUN pip3 install "ipython[notebook]"

# Install libfreetype6-dev for matplotlib installation
RUN apt-get install -y libfreetype6-dev && apt-get clean

# Install libblas-dev, liblapack-dev, gfortran for scipy installation
RUN apt-get install -y libblas-dev liblapack-dev gfortran && apt-get clean

# Install ipywidgets, matplotlib, NumPy, SciPy for Python 2
RUN pip2 install ipywidgets matplotlib numpy scipy

# Install ipywidgets, matplotlib, NumPy, SciPy for Python 3
RUN pip3 install ipywidgets matplotlib numpy scipy

# Clone K3D repository
ENV REFRESHED_K3D_AT 2016–01–10
RUN cd /tmp && git clone https://github.com/K3D-tools/K3D-jupyter.git

# Install bower for K3D installation
RUN npm install -g bower

# Install jupyter-pip for K3D installation
RUN pip2 install jupyter-pip
RUN pip3 install jupyter-pip

# Install K3D
RUN cd /tmp/K3D-jupyter && bower install --allow-root --config.interactive=false
RUN cd /tmp/K3D-jupyter && pip2 install .
RUN cd /tmp/K3D-jupyter && pip3 install .

# Delete K3D-jupyter dir
RUN rm -r /tmp/K3D-jupyter

# Expose a port
EXPOSE 7171

# Copy the 'jupyterhubscript' file to the filesystem of the container
COPY jupyterhubscript jupyterhubscript
RUN chmod 755 jupyterhubscript

CMD ./jupyterhubscript
