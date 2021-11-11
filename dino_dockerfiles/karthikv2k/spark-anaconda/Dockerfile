FROM karthikv2k/spark:latest
MAINTAINER Karthik <karthikv2k@gmail.com>

#Install Anaconda
RUN curl -s https://repo.continuum.io/archive/Anaconda2-2.5.0-Linux-x86_64.sh -o anaconda.sh
RUN chmod a+x anaconda.sh
RUN ./anaconda.sh -b
RUN ./anaconda2/bin/conda update --all -y

#Environment vaiables for Spark to use Anaconda Python and Jupyter notebook
ENV PYSPARK_PYTHON /anaconda2/bin/python2
ENV PYSPARK_DRIVER_PYTHON /anaconda2/bin/jupyter
ENV PYSPARK_DRIVER_PYTHON_OPTS "notebook --no-browser --port 8888 --ip '*'"

#Jupyter port
EXPOSE 8888
#Spark port
EXPOSE 4040

CMD ["pyspark"]
