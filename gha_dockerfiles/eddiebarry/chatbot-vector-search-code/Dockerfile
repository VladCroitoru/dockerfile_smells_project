# # conda create -n venv_name python=3.6
# # conda activate venv_name
# # conda install -c pytorch faiss-cpu
# # # linux
# # sudo apt install gcc
# # git clone https://github.com/facebookresearch/fastText.git
# # cd fastText
# # sudo pip install .
# # sudo /Users/edgarmonis/minicond/envs/venv_name/bin/pip 
# # gunicorn --worker-class gevent --bind 0.0.0.0:5001   wsgi:app --workers 2 --worker-connections 2000 --timeout 60 --preload

# FROM continuumio/miniconda3:4.9.2

# # Create the environment:
# # COPY . .
# # ADD "https://www.random.org/cgi-bin/randbyte?nbytes=10&format=h" skipcache

# COPY . /WHO-FAQ-Chitchat-API

# WORKDIR /WHO-FAQ-Chitchat-API

# RUN conda env create -f env.yaml

# RUN git clone https://github.com/facebookresearch/fastText.git

# WORKDIR /WHO-FAQ-Chitchat-API/fastText
# RUN apt-get update
# RUN apt install -y g++

# RUN /opt/conda/envs/myenv/bin/pip install .

# WORKDIR /WHO-FAQ-Chitchat-API

# RUN /opt/conda/envs/myenv/bin/pip install -r requirements.txt

# # converting the latest script QnAs into consumable files:
# RUN ["conda", "run", "-n", "myenv", "python", "./production_data/excel_script_2_json.py"]

# # downloading lexical model:
# RUN ["conda", "run", "-n", "myenv", "python", "-m", "spacy", "download", "en_core_web_sm"]

# # RUN ["conda", "run", "--no-capture-output", "-n", "myenv", "python", "download_weights.py"]

# # # updating the indexed sentences and the JSON datasets from the Excel script:
# # RUN ["conda", "run", "--no-capture-output", "-n", "myenv", "python", "demo.py"]

# # conda run --no-capture-output -n myenv python download_weights.py
# # # Make RUN commands use the new environment:
# # SHELL ["conda", "run", "-n", "myenv", "/bin/bash", "-c"]

# # # Make sure the environment is activated:
# # RUN echo "Make sure flask is installed:"
# # RUN python -c "import flask"

# # # The code to run when container is started:
# # COPY run.py .

# # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# # making the image OpenShift-compatible:

# # creating a random user belonging to a random group to run the application:
# ARG DOCKER_UID=1000
# ARG DOCKER_GID=1000
# RUN groupadd --gid ${DOCKER_GID} lxp \
#     || echo "Group with ID ${DOCKER_GID} already exists." \
#     && useradd --create-home --home-dir /home/lxp --uid ${DOCKER_UID} --gid ${DOCKER_GID} lxp \
#     || echo "Skip user creation (user with ID ${DOCKER_UID} already exists?)"
# # making sure that the initial directories have the correct permissions for
# # OpenShift - OpenShift will run any pod with a random user (random UID)
# # belonging to group 0 (GID = 0):
# WORKDIR /opt/conda
# RUN chgrp -R 0 . && chmod -R g=u .
# WORKDIR /WHO-FAQ-Chitchat-API
# RUN chgrp -R 0 . && chmod -R g=u .
# # settng a random user ID and group ID so that OpenShift knows we don't run
# # the process as root:
# USER ${DOCKER_UID}:${DOCKER_GID}
# # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# # CMD sh "./daemon.sh"
# CMD conda run --no-capture-output -n myenv gunicorn --worker-class gevent --bind 0.0.0.0:5001 wsgi:app --workers 2 --worker-connections 2000 --timeout 60 --preload


FROM ubuntu:focal as app

# System requirements.
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
	apt-get upgrade -qy
RUN apt-get install --yes \
	git \
	language-pack-en \
	python3-venv \
	python3.8-dev \
	python3.8-venv \
	build-essential \
	libffi-dev \
	libmysqlclient-dev \
	libxml2-dev \
	libxslt1-dev \
	libjpeg-dev \
	libssl-dev

RUN rm -rf /var/lib/apt/lists/*

ENV VIRTUAL_ENV=/venv
RUN python3.8 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install pip==20.2.3 setuptools==50.3.0 nodeenv

# Use UTF-8.
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# Working directory will be root of repo.
WORKDIR /app/vector

# Copy just Python requirements & install them.
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy over rest of code.
# We do this AFTER requirements so that the requirements cache isn't busted
# every time any bit of code is changed.
COPY . .

# RUN python ./production_data/excel_script_2_json.py
# RUN python ./demo.py

EXPOSE 8000

FROM app as newrelic
RUN pip install newrelic

# CMD tail -f /dev/null
CMD sh "./daemon.sh"

# CMD newrelic-admin run-program gunicorn --bind=0.0.0.0:28381 --workers 1 --max-requests=1000 -c course_discovery/docker_gunicorn_configuration.py course_discovery.wsgi:application
