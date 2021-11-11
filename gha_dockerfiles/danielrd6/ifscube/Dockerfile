FROM continuumio/miniconda3 

WORKDIR /ifscube
COPY . /ifscube/

# Create environment
RUN conda env create -f environment.yml
SHELL ["conda", "run", "-n", "ifscube", "/bin/bash", "-c"]

RUN pip install .
RUN pytest
WORKDIR /ifscube/ifscube/examples
RUN specfit --overwrite -c halpha_gauss.cfg manga_onedspec.fits
RUN cubefit --overwrite -c halpha_cube.cfg ngc3081_cube.fits
