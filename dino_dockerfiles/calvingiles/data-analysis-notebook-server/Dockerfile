FROM ipython/scipyserver

MAINTAINER Calvin Giles <calvin.giles@gmail.com>

# Create install folder
RUN mkdir /install_files

# Update aptitude with new repo
RUN apt-get update

# Install software
RUN apt-get install -y git

# Install postgres libraries and python dev libraries so we install psycopg2 later
RUN apt-get update && apt-get install libpq-dev python-dev

# install python requirements
COPY requirements.txt /install_files/requirements.txt
RUN pip2 install -r /install_files/requirements.txt
RUN pip3 install -r /install_files/requirements.txt

# Create known_hosts
RUN mkdir -p /root/.ssh
RUN touch /root/.ssh/known_hosts
# Add github key
RUN ssh-keyscan github.com >> /root/.ssh/known_hosts

# Install pyspark config to notebook
COPY 00-pyspark-setup.py /root/.ipython/profile_default/startup/00-pyspark-setup.py

# install spark standalone
RUN apt-get update && apt-get install -y wget default-jdk
WORKDIR /install_files
RUN wget -q http://wwwftp.ciril.fr/pub/apache/spark/spark-1.4.0/spark-1.4.0-bin-hadoop2.6.tgz
RUN tar -zxvf spark-1.4.0-bin-hadoop2.6.tgz
RUN rm spark-1.4.0-bin-hadoop2.6.tgz
RUN mv spark-1.4.0-bin-hadoop2.6 /usr/local/spark/
RUN pip2 install py4j
ENV PATH=/usr/local/spark/python/:$PATH
ENV SPARK_HOME '/usr/local/spark'
#ENV PYSPARK_SUBMIT_ARGS --master

# Put the working directory back to notebooks at the end
WORKDIR /notebooks
