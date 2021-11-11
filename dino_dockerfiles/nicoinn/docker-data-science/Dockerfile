FROM ubuntu:18.04

ENV SCALA_VERSION 2.11.12
ENV SPARK_VERSION 2.3.1

#Set the time zone
ENV TZ=Europe/Stockholm
ENV PORT=8888

#Commit the time zone configuration
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone


COPY pkglist_* /

RUN apt-get update && apt-get install -y --no-install-recommends `cat pkglist_apt | awk '($1!~/^#/) && ($1!~/^$/) {print $1}' ` \
               && apt-get clean && rm -rf /var/lib/apt/lists/*


#Download and install Scala
RUN curl -sO https://downloads.lightbend.com/scala/${SCALA_VERSION}/scala-${SCALA_VERSION}.deb && dpkg -i scala-${SCALA_VERSION}.deb && rm -rf scala-${SCALA_VERSION}.deb

#Download and install Spark for local use
RUN curl -s  http://apache.mirrors.spacedump.net/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop2.7.tgz | tar -xzf -
ENV SPARK_HOME=/spark-${SPARK_VERSION}-bin-hadoop2.7

#Install Jupyter (Jupyter runs in Python3 even when using the Python2 kernel)
RUN python3 -m pip install -U setuptools wheel && python -m pip install -U setuptools wheel  && python3 -m pip install -U jupyter jupyterlab

#Install Python 2 packages
RUN python2 -m pip install -U `cat /pkglist_python | awk '($1!~/^#/) && ($1!~/^$/) {print $1}'`

#Install Python 3 packages
RUN python3 -m pip install -U `cat /pkglist_python | awk '($1!~/^#/) && ($1!~/^$/) {print $1}'`

#Install Jupyter kernels
RUN pip install ipykernel \
	&& python3 -m pip install ipykernel sparkmagic spylon-kernel \
    	&& python3 -m ipykernel install \
    	&& python2 -m ipykernel install \
	&& python3 -m spylon_kernel install

RUN mkdir /data

COPY jupyter_notebook_config.py /root/.jupyter/

RUN jupyter nbextension enable --py --sys-prefix widgetsnbextension

WORKDIR /data
CMD /usr/local/bin/jupyter lab --port=$PORT --ip=0.0.0.0 --no-browser --allow-root --custom_display_url="prout"
