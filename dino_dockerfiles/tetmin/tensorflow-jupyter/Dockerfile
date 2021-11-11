FROM debian:jessie
MAINTAINER Tom Etminan

# Run all ubuntu updates and apt-get installs
RUN export DEBIAN_FRONTEND=noninteractive && \
	apt-get update && \
	apt-get upgrade -y && \
	apt-get install -y git \
		wget \
		bzip2 \
		build-essential \
		python-dev \
		gfortran \
	&& apt-get clean
RUN apt-get install -y libx11-dev


# Create conda user, get anaconda by web or locally
RUN useradd --create-home --home-dir /home/condauser --shell /bin/bash condauser

# Link in our build files to the docker image
ADD src/ /tmp

RUN /tmp/get_anaconda.sh

# Run all python installs
# Perform any cleanup of the install as needed
USER condauser
RUN /tmp/install.sh

# Copy notebook config into ipython directory
# Make sure our user owns the directory
USER root
RUN  apt-get --purge -y autoremove wget && \
	cp /tmp/ipython_notebook_config.py /home/condauser/.ipython/profile_default/ && \
	cp /tmp/matplotlib_nb_init.py /home/condauser/.ipython/profile_default/startup && \
	chown condauser:condauser /home/condauser -R

# Set persistent environment variables for python3 and python2
ENV PY2PATH=/home/condauser/anaconda3/envs/python2/bin
ENV PY3PATH=/home/condauser/anaconda3/bin

# Install the python2 ipython kernel
#RUN $PY2PATH/python $PY2PATH/ipython kernelspec install-self

# Setup our environment for running the ipython notebook
# Setting user here makes sure ipython notebook is run as user, not root
EXPOSE 8888
USER condauser
ENV HOME=/home/condauser
ENV SHELL=/bin/bash
ENV USER=condauser
WORKDIR /home/condauser/notebooks


RUN /bin/bash -c "$PY3PATH/pip install --upgrade https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.11.0rc0-cp35-cp35m-linux_x86_64.whl"
RUN /bin/bash -c "$PY3PATH/pip install Pillow==2.9.0 matplotlib sklearn keras"

USER root
RUN mkdir /notebook
RUN chown condauser:condauser /notebook



VOLUME /notebook
WORKDIR /notebook



USER root

CMD $PY3PATH/jupyter notebook --no-browser --ip=0.0.0.0
CMD $PY3PATH/tensorboard --logdir='/tmp/tflearn_logs' --host 0.0.0.0
