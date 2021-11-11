FROM ipython/scipyserver

MAINTAINER Calvin Giles <calvin.giles@gmail.com>

# Create install folder
RUN mkdir /install_files

# Install postgres libraries and python dev libraries so we install psycopg2 later
RUN apt-get update
RUN apt-get install libpq-dev python-dev

# install python requirements
COPY requirements.txt /install_files/requirements.txt
RUN pip2 install -r /install_files/requirements.txt
RUN pip3 install -r /install_files/requirements.txt

# Set the working directory to notebooks
WORKDIR /notebooks
