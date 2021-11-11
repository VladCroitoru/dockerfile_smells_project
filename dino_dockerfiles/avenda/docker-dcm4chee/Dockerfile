
#
# DCM4CHEE - Open source picture archive and communications server (PACS)
#
FROM ubuntu:14.04
MAINTAINER AI Analysis, Inc <admin@aianalysis.com>

# Load the stage folder, which contains the setup scripts.
#
ENV DCM_ARC_VERSION=2.18.0
ENV DCM_ARR_VERSION=3.0.11
ENV DCM4CHEE_HOME=/var/local/dcm4chee

ADD stage stage

RUN mkdir -p ${DCM4CHEE_HOME}

WORKDIR ${DCM4CHEE_HOME}

RUN apt-get update && apt-get install -yq --no-install-recommends \
curl zip unzip openjdk-6-jdk python mysql-client

# Download the binary package for DCM4CHEE
RUN curl -G http://superb-dca2.dl.sourceforge.net/project/dcm4che/dcm4chee/${DCM_ARC_VERSION}/dcm4chee-${DCM_ARC_VERSION}-mysql.zip > /stage/dcm4chee-${DCM_ARC_VERSION}-mysql.zip
RUN unzip -q /stage/dcm4chee-${DCM_ARC_VERSION}-mysql.zip
ENV DCM_DIR=${DCM4CHEE_HOME}/dcm4chee-${DCM_ARC_VERSION}-mysql

# Download the binary package for JBoss
RUN curl -G http://superb-dca2.dl.sourceforge.net/project/jboss/JBoss/JBoss-4.2.3.GA/jboss-4.2.3.GA-jdk6.zip > /stage/jboss-4.2.3.GA-jdk6.zip
RUN unzip -q /stage/jboss-4.2.3.GA-jdk6.zip
ENV JBOSS_DIR=${DCM4CHEE_HOME}/jboss-4.2.3.GA

# Download the Audit Record Repository (ARR) package
RUN curl -G http://superb-dca2.dl.sourceforge.net/project/dcm4che/dcm4chee-arr/${DCM_ARR_VERSION}/dcm4chee-arr-${DCM_ARR_VERSION}-mysql.zip > /stage/dcm4chee-arr-${DCM_ARR_VERSION}-mysql.zip
RUN unzip -q /stage/dcm4chee-arr-${DCM_ARR_VERSION}-mysql.zip
ENV ARR_DIR ${DCM4CHEE_HOME}/dcm4chee-arr-${DCM_ARR_VERSION}-mysql

# Copy files from JBoss to dcm4chee
RUN ${DCM_DIR}/bin/install_jboss.sh ${JBOSS_DIR} > /dev/null
RUN ls ${ARR_DIR}
# Copy files from the Audit Record Repository (ARR) to dcm4chee
RUN ${DCM_DIR}/bin/install_arr.sh ${ARR_DIR}

RUN chmod 755 /stage/*.bash
RUN chmod 755 /stage/*.py

CMD ["/stage/start.bash"]
