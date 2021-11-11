FROM solr:5

ENV VFB_OWL_VERSION=Current

ENV PDBserver=http://pdb.VirtualFlyBrain.org

RUN chmod -R 777 /opt/solr

ENV WORKSPACE=/opt/VFB

ENV SOLR_HOME=/opt/VFB/OLS/ols-solr/src/main/solr-5-config
ENV solr.data.dir=/opt/solr/server/solr

USER root

RUN apt-get -qq update && \
  apt-get -qq -y install git maven openjdk-8-jdk apt-transport-https tree apt-utils nano && \
  rm -rf /var/lib/apt/lists/*
  
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64

RUN echo Building OLS && \
mkdir -p /opt/VFB && \
cd /opt/VFB && \
git clone --quiet https://github.com/Robbie1977/OLS.git

COPY application-vfb.properties ${WORKSPACE}/OLS/ols-apps/ols-solr-app/src/main/resources/application-vfb.properties

RUN cd /opt/VFB/OLS && \
mvn -q clean package

COPY loadOLS.sh /opt/VFB/loadOLS.sh

RUN chmod -R 777 /opt || :

RUN chmod +x /opt/VFB/loadOLS.sh

RUN curl https://repo.anaconda.com/pkgs/misc/gpgkeys/anaconda.asc | gpg --dearmor > conda.gpg && \
  install -o root -g root -m 644 conda.gpg /etc/apt/trusted.gpg.d/
  
RUN echo "deb [arch=amd64] https://repo.anaconda.com/pkgs/misc/debrepo/conda stable main" > /etc/apt/sources.list.d/conda.list

RUN apt-get -qq update && \
  apt-get -qq -y install conda
  
ENV PATH=/opt/conda/bin:/opt/conda/envs/env/bin:$PATH

#USER $SOLR_USER

ENTRYPOINT ["/opt/VFB/loadOLS.sh"]
