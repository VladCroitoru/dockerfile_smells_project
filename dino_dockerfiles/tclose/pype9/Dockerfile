#
# A Docker image for running PyPe9 examples
#
# Steps to run the examples using Docker:
# 
#  1. Install Docker (see https://docs.docker.com/engine/installation/)
#
#  2. Pull the Pype9 "Docker image"
#
#        docker pull tclose/pype9
#
#  3. Create a "Docker container" from the downloaded image 
#
#        docker run -v `pwd`/<your-local-output-dir>:/home/docker/output -t -i tclose/pype9 /bin/bash
#
#    This will create a folder called <your-local-output-dir> in the
#    directory you are running the docker container, which you can access
#    from your host computer (i.e. outside of the container) and view the
#    output figures from.
#
#  4. From inside the running container, you will be able to run pype9, e.g.
#
#        pype9 simulate \
#	 	     ~/nineml-catalog/xml/neuron/HodgkinHuxley#PyNNHodgkinHuxleyProperties \
#	 	     nest 500.0 0.001 \
#	 	     --init_value v 65 mV \
#	 	     --init_value m 0.0 unitless \
#	 	     --init_value h 1.0 unitless \
#	 	     --init_value n 0.0 unitless \
#	 	     --record v ~/output/hh-v.neo.pkl
#
#         pype9 plot ~/output/hh-v.neo.pkl --save ~/output/hh-v.png
#
#    Supply the '--help' option to see a full list of options for each example.
#
#  5. Edit the xml descriptions in the ~/catalog directory to alter the
#     simulated models as desired.
#

FROM neuralensemble/simulationx
MAINTAINER tom.g.close@gmail.com

# Install Python library
USER root
RUN apt-get update; apt-get install -y python-lxml libhdf5-serial-dev \
                                       libyaml-dev

USER docker

# Install 9ML Python
RUN PATH=$PATH:$VENV/bin pip install git+https://github.com/INCF/nineml-python.git@pype9_port

# Install 9ML catalog
RUN git clone --branch merging_with_master https://github.com/INCF.git $HOME/nineml-catalog
RUN PATH=$PATH:$VENV/bin pip install $HOME/nineml-catalog

# Install Pype9
RUN PATH=$PATH:$VENV/bin pip install git+https://github.com/NeuralEnsemble/pype9.git

# Set up bashrc and add welcome message
RUN sed 's/#force_color_prompt/force_color_prompt/' $HOME/.bashrc > $HOME/tmp; mv $HOME/tmp $HOME/.bashrc; rm tmp;
RUN echo "echo \"Type 'pype9 help' for instructions on how to run pype9\"" >> $HOME/.bashrc
RUN echo "echo \"See $HOME/catalog for example 9ML models\"" >> $HOME/.bashrc

WORKDIR $HOME
