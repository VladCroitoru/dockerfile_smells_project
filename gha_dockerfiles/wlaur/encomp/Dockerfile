FROM continuumio/miniconda3

WORKDIR /app

# copy environment specification and requirements and create the env
COPY environment.yml requirements.txt requirements-dev.txt ./
RUN conda env create -f environment.yml

# activate the env automatically for each new shell
RUN echo "source activate encomp-env" > ~/.bashrc
ENV PATH /opt/conda/envs/encomp-env/bin:$PATH

# install coolprop
# TODO: remove this once coolprop supports Python 3.9
RUN conda install conda-forge::coolprop


# copy local whl-file and install
# use wildcard since filename contains version number
# make sure that the latest version is the only file in the /dist folder
# run "python utils.py build" to create this file
COPY dist/encomp-* .

RUN pip install encomp-*.whl

# run the docker container with
# docker run -it encomp
