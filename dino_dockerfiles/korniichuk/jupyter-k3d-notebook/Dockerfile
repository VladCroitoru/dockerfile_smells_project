# Name: korniichuk/jupyter-k3d-notebook
# Short Description: Jupyter Notebook with K3D
# Full Description: The korniichuk/jupyter-notebook Docker image with K3D.
# Version: 0.2a1

FROM korniichuk/jupyter-notebook:latest

MAINTAINER Ruslan Korniichuk <ruslan.korniichuk@gmail.com>

USER root

# Clone K3D repository
ENV REFRESHED_AT 2015–12–11
RUN git clone https://github.com/K3D-tools/K3D-jupyter.git

# Install K3D
RUN cd K3D-jupyter && bower install --allow-root --config.interactive=false
RUN cd K3D-jupyter && pip install .
RUN cd K3D-jupyter && /opt/conda/envs/python2/bin/pip install .

# Copy /home/jovyan/work/K3D-jupyter/examples dir to /home/jovyan/work dir
RUN cp -a /home/jovyan/work/K3D-jupyter/examples /home/jovyan/work

# Change the owner of /home/jovyan/work/examples dir to jovyan (recursively)
RUN chown -R jovyan /home/jovyan/work/examples

# Delete K3D-jupyter dir
RUN rm -r /home/jovyan/work/K3D-jupyter

USER jovyan
