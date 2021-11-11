FROM gettyimages/spark:2.3.0-hadoop-2.8
MAINTAINER Agustin C. Caminero

RUN apt-get update \
 && apt-get install -y nano wget bzip2\
 && apt-get clean

# Install Anaconda (which includes Jupyter)
RUN echo 'Installing Anaconda'
RUN wget https://repo.continuum.io/archive/Anaconda2-5.0.1-Linux-x86_64.sh \
 && /bin/bash ./Anaconda2-5.0.1-Linux-x86_64.sh -b -p /opt/anaconda \ 
 && rm -rf Anaconda2-5.0.1-Linux-x86_64.sh 



# Download this to integrate Spark and Kafka
RUN echo 'Downloading Spark-Kafka integration'
RUN wget http://central.maven.org/maven2/org/apache/spark/spark-streaming-kafka-0-8-assembly_2.11/2.3.0/spark-streaming-kafka-0-8-assembly_2.11-2.3.0.jar

# Disable token authentication for Jupyter Notebook
RUN mkdir -p /root/.jupyter
RUN touch /root/.jupyter/jupyter_notebook_config.py
RUN echo "c.NotebookApp.token = ''" >> /root/.jupyter/jupyter_notebook_config.py
RUN echo "c.NotebookApp.password = ''" >> /root/.jupyter/jupyter_notebook_config.py

# Set Environment Variable to use ipython with PySpark
RUN echo 'Set environment variables'
RUN mkdir -p /media/notebooks
ENV PYSPARK_PYTHON /opt/anaconda/bin/python
ENV PATH $PATH:/opt/anaconda/bin

# Findspark needed to run Spark using notebooks
RUN [ "/bin/bash", "-c", "source /opt/anaconda/bin/activate &&  pip install findspark " ]


