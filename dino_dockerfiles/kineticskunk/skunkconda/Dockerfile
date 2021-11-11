FROM openshift/jenkins-slave-base-centos7
MAINTAINER CI Team <ci@vodacom.co.za>

ARG ANACONDA_VERSION="5.0.1"
ARG MIRROR="https://repo.continuum.io/archive"

ENV APPLICATION anaconda
ENV ANACONDA_VERSION $ANACONDA_VERSION
ENV ANACONDA_INSTALLER Anaconda3-${ANACONDA_VERSION}-Linux-x86_64.sh
ENV USER $APPLICATION
ENV APP_ROOT /opt
ENV FILES_LOCATION=roles/ds-tools/files

LABEL io.k8s.description="A Anancoda Jenkins Slave Container." \
    io.k8s.display-name="Anaconda ${ANACONDA_VERSION}" \
    io.openshift.expose-services="8080:http" \
    io.openshift.tags="python,anaconda,conda,conda-build,java,dataprocessing"

RUN yum install -y bzip2 python3-devel gcc && yum clean all

# Install conda
RUN curl -o ${APP_ROOT}/anaconda.sh ${MIRROR}/${ANACONDA_INSTALLER} && \
    sh ${APP_ROOT}/anaconda.sh -b -p ${APP_ROOT}/conda && \
    rm ${APP_ROOT}/anaconda.sh
ENV PATH ${APP_ROOT}/conda/bin:$PATH
RUN conda install -n root pyspark

COPY requirements.txt /home/Jenkins/
COPY install-junit2html.sh /home/Jenkins/

RUN sh /home/Jenkins/install-junit2html.sh

RUN chown -R 1001:0 $HOME && \
	chmod -R g+rw $HOME && \
	chown -R 1001:0 /opt && \
	chmod -R g+rw /opt

USER 1001

RUN pip install --user -r /home/Jenkins/requirements.txt
RUN yum remove -y bzip2 curl