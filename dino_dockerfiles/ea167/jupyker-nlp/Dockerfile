# NOTES:
#   1. You need an Nvidia GPU to run this Docker image.
#           Otherwise use the alternative ea167/jupyker-cpu
#   2. Install the nvidia-docker wrapper on your computer to launch the image
#           https://github.com/NVIDIA/nvidia-docker
#           Warning: can't be run on Mac unfortunately, only Linux and Windows (Aug 2017)
#
# To run:
# 	nvidia-docker run -it -d -p=6006:6006 -p=8888:8888 -v=~/DockerShared/JupykerShared:/host  ea167/jupyker-nlp
#
# http://localhost:8888 for Jupyter Notebook
# http://localhost:6006 for TensorBoard
#
# Built for Nvidia GPUs
#
# To run tensorboard:
# 	tensorboard --logdir=path/to/logs
# 	where path/to/logs is typically related to
# 		file_writer = tf.summary.FileWriter('/path/to/logs', sess.graph)

# NOTE: to build:
# 	Use Docker Automated Build,
# 	OR
# 		Run  ' docker build -t ea167/jupyker-nlp . ' to build it
# 		Then ' docker login '
# 	   		 ' docker push ea167/jupyker-nlp '

FROM ea167/jupyker
LABEL maintainer="Eric Amram <eric dot amram at gmail dot com>"


# NLP related:
# NLTK
RUN pip3 --no-cache-dir install \
    nltk \
    gensim
# Download all NLTK data
RUN python3 -m nltk.downloader -d /usr/local/share/nltk_data all \
 && echo "export NLTK_DATA=/usr/local/share/nltk_data" >> /root/.bashrc

# Spacy
RUN pip3 --no-cache-dir install  spacy
# Download available languages
RUN python3 -m spacy download en \
 && python3 -m spacy download fr \
 && python3 -m spacy download de

# ConceptNet
RUN pip3 --no-cache-dir install  conceptnet
# Download all models
### RUN python3 -m conceptnet.models import *


CMD jupyter notebook --allow-root --no-browser --ip=* --NotebookApp.password="$PASSWD" \
    & /bin/bash
