# Use hadleyverse as it has the legacy rJava installs tidyverse cut
FROM rocker/verse:latest

# Versioning
ENV SPARK_VERSION 2.0.2
ENV SPARKLYR_VERSION 0.5.5
ENV DPLYR_VERSION 0.5.0

# Add CRAN mirror
RUN echo 'options(repos = c(CRAN = "https://cran.rstudio.com"))' > .Rprofile

# Install dplyr, sparklyr, spark via sparklyr
Run R -e 'devtools::install_version("dplyr", version = Sys.getenv("DPLYR_VERSION"))'
RUN R -e 'devtools::install_version("sparklyr", version = Sys.getenv("SPARKLYR_VERSION"))'
RUN R -e 'str_spark_version = Sys.getenv("SPARK_VERSION"); sparklyr::spark_install(str_spark_version)'

# Tell rserver which R install to use and move spark install to rstudio user
RUN echo 'rsession-which-r=/usr/local/bin/R' > /etc/rstudio/rserver.conf \
  && mkdir /home/rstudio/.cache \
  && mv /root/.cache/spark/ /home/rstudio/.cache \
  && chown -R rstudio:rstudio /home/rstudio/.cache \
  && mkdir /root/main

ENV RSTUDIO_SPARK_HOME /home/rstudio/.cache/spark/spark-2.0.2-bin-hadoop2.7

# Install supervisor as several processes need to be run
RUN apt-get update && apt-get install -y openssh-server apache2 supervisor

RUN mkdir -p /var/lock/apache2 /var/run/apache2 /var/run/sshd /var/log/supervisor

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

COPY spark-defaults.conf $RSTUDIO_SPARK_HOME/conf

CMD ["/usr/bin/supervisord"]
