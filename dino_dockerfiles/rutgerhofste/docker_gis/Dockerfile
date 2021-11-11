FROM rutgerhofste/docker_python_envs:stable
MAINTAINER Rutger Hofste <rutgerhofste@gmail.com>


# ##########################  Python ##########################################
# Make Conda Forge Highest Priority
RUN conda config --add channels conda-forge
RUN conda config --append channels esri

COPY requirementsPython.txt .
COPY requirementsPython27.txt .
COPY requirementsPython35.txt .
COPY requirementsPython36.txt .
COPY requirementsPython36arc.txt .

RUN conda install --file requirementsPython.txt
RUN conda install --name python27 --file requirementsPython27.txt
RUN conda install --name python35 --file requirementsPython35.txt
RUN conda install --name python36 --file requirementsPython36.txt
RUN conda install --name python36arc --file requirementsPython36arc.txt

# Make command line tool accessible to root python (note that the path for cli will be part of root env)
RUN pip install earthengine-api
RUN [ "/bin/bash", "-c", "source activate python27 && pip install earthengine-api" ]
RUN [ "/bin/bash", "-c", "source activate python35 && pip install earthengine-api" ]


# ##########################  Command Line ####################################
# Google-cloud-sdk 
# https://cloud.google.com/sdk/docs/quickstart-debian-ubuntu
RUN export CLOUD_SDK_REPO="cloud-sdk-xenial" && \
    echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && \
    apt-get update -y && apt-get install google-cloud-sdk -y

# Reinstall core jupyter and conda extension. better be safe than sorry 
# RUN conda install jupyter -y
# RUN conda install nb_conda -y
# RUN jupyter nbextension enable arcgis --py --sys-prefix

# ##########################  GDAL ############################################
# GDAL 1.1.x system intall
# not used in this image. See older commits for gdal-bin cli. 

# GDAL 2.2.4 for python
RUN conda install --name python27 gdal -y
RUN conda install --name python35 gdal -y


# ##########################  Tests ###########################################
COPY tests/test_python27.py /
RUN [ "/opt/anaconda3/envs/python27/bin/python", "-u", "./test_python27.py" ]

COPY tests/test_python35.py /
RUN [ "/opt/anaconda3/envs/python35/bin/python", "-u", "./test_python35.py" ]

COPY tests/test_python36.py /
RUN [ "/opt/anaconda3/envs/python36/bin/python", "-u", "./test_python36.py" ]

COPY tests/test_python36arc.py /
RUN [ "/opt/anaconda3/envs/python36arc/bin/python", "-u", "./test_python36arc.py" ]


# Todo

# Since there is a conflict of netcdf4 and gdal, is it necessary to install netCDF4 separately ?
# Posted question here: https://github.com/Unidata/netcdf4-python/issues/790#issuecomment-379318057
