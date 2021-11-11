FROM mcristinagrosu/bigstep_hdfs_datalake_ubuntu

# Install Spark 2.1.0
RUN cd /opt && wget http://d3kbcqa49mib13.cloudfront.net/spark-2.1.0-bin-hadoop2.7.tgz
RUN tar xzvf /opt/spark-2.1.0-bin-hadoop2.7.tgz
RUN rm  /opt/spark-2.1.0-bin-hadoop2.7.tgz

RUN curl -L -C - -b "oraclelicense=accept-securebackup-cookie" -O http://download.oracle.com/otn-pub/java/jce/8/jce_policy-8.zip
RUN apt-get install -y unzip
RUN unzip jce_policy-8.zip
RUN cp UnlimitedJCEPolicyJDK8/US_export_policy.jar /opt/jdk1.8.0_72/jre/lib/security/ && cp UnlimitedJCEPolicyJDK8/local_policy.jar /opt/jdk1.8.0_72/jre/lib/security/
RUN rm -rf UnlimitedJCEPolicyJDK8

# Spark pointers
ENV SPARK_HOME /opt/spark-2.1.0-bin-hadoop2.7
ENV R_LIBS_USER $SPARK_HOME/R/lib:/opt/conda/envs/ir/lib/R/library:/opt/conda/lib/R/library
ENV PYTHONPATH $SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.8.2.1-src.zip

RUN mv /spark-2.1.0-bin-hadoop2.7 /opt/ 
RUN mkdir -p /user && mkdir -p /user/notebooks && mkdir -p /user/datasets

ADD entrypoint.sh /
ADD core-site.xml.datalake /opt/spark-2.1.0-bin-hadoop2.7/conf/
ADD core-site.xml.datalake.integration /opt/spark-2.1.0-bin-hadoop2.7/conf/

ADD krb5.conf.integration /etc/
ADD krb5.conf /etc/

RUN chmod 777 /entrypoint.sh
ADD spark-defaults.conf /opt/spark-2.1.0-bin-hadoop2.7/conf/spark-defaults.conf.template

ENV HADOOP_HOME /opt/hadoop
ENV HADOOP_CONF_DIR /opt/hadoop/etc/hadoop

ENV CONDA_DIR /opt/conda
ENV PATH $CONDA_DIR/bin:$PATH
ENV PATH $PATH:/$SPARK_HOME/bin/

RUN cd /opt && \
    wget https://repo.continuum.io/miniconda/Miniconda2-4.2.12-Linux-x86_64.sh && \ 
    /bin/bash Miniconda2-4.2.12-Linux-x86_64.sh  -b -p $CONDA_DIR && \
     rm -rf  Miniconda2-4.2.12-Linux-x86_64.sh

RUN export PATH=$PATH:/$CONDA_DIR/bin

# Install Jupyter notebook 
RUN $CONDA_DIR/bin/conda install --yes \
    'notebook' && \
    $CONDA_DIR/bin/conda clean -yt
    
RUN $CONDA_DIR/bin/jupyter notebook  --generate-config --allow-root

RUN $CONDA_DIR/bin/conda install -c conda-forge nb_conda
RUN $CONDA_DIR/bin/python -m nb_conda_kernels.install --disable --prefix=$CONDA_DIR && \
    $CONDA_DIR/bin/conda clean -yt
RUN pip install nbpresent
RUN jupyter nbextension install nbpresent --py --overwrite
RUN jupyter-nbextension enable nb_conda --py --sys-prefix
RUN jupyter-serverextension enable nb_conda --py --sys-prefix
RUN jupyter-nbextension enable nbpresent --py --sys-prefix
RUN jupyter-serverextension enable nbpresent --py --sys-prefix

#Add progress bar extension

RUN pip install jupyter-spark
RUN jupyter serverextension enable --py jupyter_spark
RUN jupyter nbextension install --py jupyter_spark
RUN jupyter nbextension enable --py jupyter_spark
RUN jupyter nbextension enable --py widgetsnbextension
RUN pip install lxml

#Install Scala Spark kernel
ENV SBT_VERSION 0.13.15
ENV SBT_HOME /usr/local/sbt
ENV PATH ${PATH}:${SBT_HOME}/bin

# Install sbt
RUN wget "http://repo.bigstepcloud.com/bigstep/datalab/sbt-0.13.11.tgz"
RUN tar -xvf /sbt-0.13.11.tgz 
RUN mv /sbt /usr/local/ && echo -ne "- with sbt $SBT_VERSION\n" >> /root/.built

    
#Install Python3 packages
RUN cd /root && $CONDA_DIR/bin/conda install --yes \
    'ipywidgets' \
    'pandas' \
    'matplotlib' \
    'scipy' \
    'seaborn' \
    'scikit-learn' && \
    $CONDA_DIR/bin/conda clean -yt
    
RUN $CONDA_DIR/bin/conda config --set auto_update_conda False

RUN CONDA_VERBOSE=3 $CONDA_DIR/bin/conda create --yes -p $CONDA_DIR/envs/python3 python=3.5 ipython ipywidgets pandas matplotlib scipy seaborn scikit-learn
RUN bash -c '. activate $CONDA_DIR/envs/python3 && \
    python -m ipykernel.kernelspec --prefix=/opt/conda && \
    . deactivate'
    
RUN wget https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64 -O /root/jq-linux64

RUN chmod +x /root/jq-linux64
RUN /root/jq-linux64 --arg v "$CONDA_DIR/envs/python3/bin/python"         '.["env"]["PYSPARK_PYTHON"]=$v' /opt/conda/share/jupyter/kernels/python3/kernel.json > /tmp/kernel.json &&   \
    mv /tmp/kernel.json /opt/conda/share/jupyter/kernels/python3/kernel.json

#Install R kernel and set up environment
RUN $CONDA_DIR/bin/conda config --add channels r
RUN $CONDA_DIR/bin/conda install --yes -c r r-essentials r-base r-irkernel r-irdisplay r-ggplot2 r-repr r-rcurl
RUN $CONDA_DIR/bin/conda create --yes  -n ir -c r r-essentials r-base r-irkernel r-irdisplay r-ggplot2 r-repr r-rcurl

RUN mkdir -p /opt/conda/share/jupyter/kernels/scala
COPY kernel.json /opt/conda/share/jupyter/kernels/scala/

RUN cd /root && wget http://central.maven.org/maven2/com/google/collections/google-collections/1.0/google-collections-1.0.jar

#Solution to readline library issues for SparkR context/session
#These are commented -> TO be enabled if there are problems initializing the sparkr session
#RUN mv $CONDA_DIR/envs/python3/lib/libreadline.so.6 $CONDA_DIR/envs/python3/lib/libreadline.so.6.tmp && \
#    ln -s /lib/x86_64-linux-gnu/libreadline.so.6 $CONDA_DIR/envs/python3/lib/libreadline.so.6
#RUN mv $CONDA_DIR/envs/ir/lib/libreadline.so.6 $CONDA_DIR/envs/ir/lib/libreadline.so.6.tmp && \
#    ln -s /lib/x86_64-linux-gnu/libreadline.so.6 $CONDA_DIR/envs/ir/lib/libreadline.so.6
#RUN mv $CONDA_DIR/lib/libreadline.so.6 $CONDA_DIR/lib/libreadline.so.6.tmp && \
#    ln -s /lib/x86_64-linux-gnu/libreadline.so.6 $CONDA_DIR/lib/libreadline.so.6
#RUN mv $CONDA_DIR/pkgs/readline-6.2-2/lib/libreadline.so.6 $CONDA_DIR/pkgs/readline-6.2-2/lib/libreadline.so.6.tmp && \
#    ln -s /lib/x86_64-linux-gnu/libreadline.so.6 $CONDA_DIR/pkgs/readline-6.2-2/lib/libreadline.so.6
    
#Add Getting Started Notebooks
RUN wget http://repo.uk.bigstepcloud.com/bigstep/datalab/datalab_getting_started_in_scala__4.ipynb -O /user/notebooks/DataLab\ Getting\ Started\ in\ Scala.ipynb
RUN wget http://repo.bigstepcloud.com/bigstep/datalab/DataLab%2BGetting%2BStarted%2Bin%2BR%20%281%29.ipynb -O /user/notebooks/DataLab\ Getting\ Started\ in\ R.ipynb
RUN wget http://repo.bigstepcloud.com/bigstep/datalab/DataLab%2BGetting%2BStarted%2Bin%2BPython%20%283%29.ipynb -O /user/notebooks/DataLab\ Getting\ Started\ in\ Python.ipynb


#Add cairo-dev for R notebook
RUN apt-get update -y
RUN apt-get install -y libcairo2-dev python-cairo-dev python3-cairo-dev

# Add hive-site.xml conf for metastore configuration
ADD hive-site.xml /opt/spark-2.1.0-bin-hadoop2.7/conf/

# Change Jupyter Logo
RUN wget http://repo.bigstepcloud.com/bigstep/datalab/logo.png -O logo.png

RUN cp logo.png $CONDA_DIR/envs/python3/doc/global/template/images/logo.png && \
    cp logo.png $CONDA_DIR/envs/python3/lib/python3.5/site-packages/notebook/static/base/images/logo.png && \
    cp logo.png $CONDA_DIR/lib/python2.7/site-packages/notebook/static/base/images/logo.png && \
    cp logo.png $CONDA_DIR/doc/global/template/images/logo.png && \
    rm -rf logo.png

RUN find / -name jars
RUN cd /opt/spark-2.1.0-bin-hadoop2.7/jars/ && wget http://repo.bigstepcloud.com/bigstep/datalab/hive-schema-1.2.0.postgres.sql && \
    wget http://repo.bigstepcloud.com/bigstep/datalab/hive-txn-schema-0.13.0.postgres.sql && \
    wget http://repo.bigstepcloud.com/bigstep/datalab/hive-txn-schema-0.14.0.postgres.sql

RUN add-apt-repository "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main" && \
    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add - 
RUN apt-get update -y
RUN apt-get install -y postgresql-client

# Add Script for hashing password
ADD password.py /opt

# Download Bigstep Data Lake Client Libraries
#RUN wget https://github.com/bigstepinc/datalake-client-libraries/releases/download/untagged-9758317a72f268684537/datalake-client-libraries-1.5-SNAPSHOT.jar -P /opt/spark-2.1.0-bin-hadoop2.7/jars/
#RUN wget https://github.com/bigstepinc/datalake-client-libraries/releases/download/1.5.2/datalake-client-libraries-1.5-SNAPSHOT.jar -P /opt/spark-2.1.0-bin-hadoop2.7/jars/
# Get Spark Thrift Postgresql connector
RUN wget https://jdbc.postgresql.org/download/postgresql-9.4.1212.jar -P /opt/spark-2.1.0-bin-hadoop2.7/jars/

#Get Kafka Streaming connector
RUN wget http://central.maven.org/maven2/org/apache/spark/spark-streaming-kafka-0-10_2.10/2.1.0/spark-streaming-kafka-0-10_2.10-2.1.0.jar -P /opt/spark-2.1.0-bin-hadoop2.7/jars/

#Get Kafka Structured Streaming connector
RUN wget http://central.maven.org/maven2/org/apache/spark/spark-sql-kafka-0-10_2.10/2.1.0/spark-sql-kafka-0-10_2.10-2.1.0.jar -P /opt/spark-2.1.0-bin-hadoop2.7/jars/

# Get the examples jar in default location
RUN cp /opt/spark-2.1.0-bin-hadoop2.7/examples/jars/spark-examples_2.11-2.1.0.jar /opt/spark-2.1.0-bin-hadoop2.7/jars/spark-examples_2.11-2.1.0.jar

#Overwrite the Spark daemon file
ADD spark-daemon.sh /opt/spark-2.1.0-bin-hadoop2.7/sbin/spark-daemon.sh

#Overwrite log4j properties file
ADD log4j.properties /opt/spark-2.1.0-bin-hadoop2.7/conf/log4j.properties

RUN cd /tmp && \
    curl -sL "http://dl.bintray.com/sbt/native-packages/sbt/$SBT_VERSION/sbt-$SBT_VERSION.tgz" | gunzip | tar -x -C /usr/local && \
    echo -ne "- with sbt $SBT_VERSION\n" >> /root/.built &&\
    git clone https://github.com/apache/incubator-toree.git && \
    cd incubator-toree && \
    make dist SHELL=/bin/bash APACHE_SPARK_VERSION=2.1.0 SCALA_VERSION=2.11 && \
    mv /tmp/incubator-toree/dist/toree /opt/toree-kernel && \
    chmod +x /opt/toree-kernel && \
    rm -rf /tmp/incubator-toree 
    
RUN cp /opt/spark-2.1.0-bin-hadoop2.7/jars/commons-crypto-1.0.0.jar /opt/hadoop/share/hadoop/common/
RUN cp /opt/spark-2.1.0-bin-hadoop2.7/jars/commons-crypto-1.0.0.jar /opt/hadoop/share/hadoop/common/lib/
    
 # Get the right Toree Assembly Jar
RUN wget http://repo.bigstepcloud.com/bigstep/datalab/toree-assembly-0.2.0.dev1-incubating-SNAPSHOT.jar -O /opt/toree-kernel/lib/toree-assembly-0.2.0.dev1-incubating-SNAPSHOT.jar

ADD version.json /opt
#        SparkMaster  SparkMasterWebUI  SparkWorkerWebUI REST     Jupyter Spark		Thrift
EXPOSE    7077        8080              8081              6066    8888      4040     88   10000

ENTRYPOINT ["/entrypoint.sh"]
