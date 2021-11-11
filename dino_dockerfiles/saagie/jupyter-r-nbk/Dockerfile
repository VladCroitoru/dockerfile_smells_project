FROM jupyter/r-notebook:c7fb6660d096

MAINTAINER Saagie

ENV HADOOP_CMD /usr/bin/hadoop
ENV SPARK_HOME /opt/spark

USER root

# Install libzmq3-dev
RUN apt-get update && apt-get install -y --no-install-recommends \
    libzmq3-dev \
    unixodbc-dev \
    libssl-dev libsasl2-dev \
    libmariadb-client-lgpl-dev \
    libpq-dev \
    mpich \
    libglu1-mesa-dev && \
    rm -rf /var/lib/apt/lists/* && apt-get clean

# Impala Jars
RUN mkdir -p /usr/lib/impala/lib && cd /usr/lib/impala/lib && \
    curl -O https://downloads.cloudera.com/connectors/Cloudera_ImpalaJDBC_2.5.5.1007.zip && \
    unzip -j Cloudera_ImpalaJDBC_2.5.5.1007.zip && unzip -j Cloudera_ImpalaJDBC4_2.5.5.1007.zip && \
    rm -f *.zip

USER jovyan

# Install openjdk and r-java
RUN conda install --yes --quiet \
    'openjdk=8.0.*' \
    'r-rjava=0.9_8' && \
    conda clean -tipsy && \
    fix-permissions $CONDA_DIR

# R Database Libraries
RUN echo 'install.packages(c("RODBC", "elastic", "mongolite", "RMySQL", "RPostgreSQL", "RJDBC", "rredis", "RCassandra", "RNeo4j", "RImpala"), repos="http://cran.us.r-project.org", dependencies=TRUE)' > /tmp/packages.R && Rscript /tmp/packages.R

# R HDFS Libraries
RUN echo 'install.packages("https://github.com/RevolutionAnalytics/rhdfs/blob/master/build/rhdfs_1.0.8.tar.gz?raw=true", repos = NULL, type = "source")' > /tmp/packages.R && Rscript /tmp/packages.R

# Machine Learning Libraries
RUN echo 'install.packages(c("microbenchmark", "runit", "arules", "arulesSequences", "neuralnet", "RSNNS", "AUC", "sprint", "recommenderlab", "acepack", "clv", "cubature", "dtw", "Formula", "googleVis", "gridExtra", "gsubfn", "hash", "Hmisc", "ifultools", "latticeExtra", "locpol", "longitudinalData", "miniUI", "misc3d", "mvtsplot", "np", "packrat", "pdc", "PKI", "rsconnect", "splus2R", "sqldf", "TaoTeProgramming", "TraMineR", "TSclust", "wmtsa"), repos="http://cran.us.r-project.org", dependencies=TRUE)' > /tmp/packages.R && Rscript /tmp/packages.R

# Clean
RUN rm -f /tmp/packages.R

# Create default workdir (useful if no volume mounted)
USER root
RUN mkdir /notebooks-dir && chown 1000:100 /notebooks-dir
USER $NB_USER

# Define default workdir
WORKDIR /notebooks-dir

# Default: run without authentication
CMD ["start-notebook.sh", "--NotebookApp.token=''", "--NotebookApp.password=''"]
