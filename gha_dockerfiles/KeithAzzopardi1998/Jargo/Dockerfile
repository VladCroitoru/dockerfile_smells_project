FROM ubuntu:18.04

ENV JARGO_DIR="/jargo"
WORKDIR ${JARGO_DIR}

#get required ubuntu packages
RUN apt-get update && apt-get install -y \
  git \
  make \
  bash \
  wget \
  vim \
  zip \
  unzip \
  screen \
  openjdk-11-jdk \
  gnupg2 \
  apt-transport-https \
  build-essential \
  gcc \
  libpq-dev \
  python3 \
  python3-venv \
  python-dev python3-dev \
  python-pip python3-pip \
  python-wheel python3-wheel \
  libderby-java \
  libderbyclient-java
  
RUN pip3 install --upgrade pip wheel setuptools

#set bash as the default shell
RUN usermod --shell /bin/bash root

# #get UM packages
# RUN echo "deb https://guinevere-ict.research.um.edu.mt/packages-um/ bionic main" |  tee /etc/apt/sources.list.d/jb.list
# RUN wget -q -O - http://guinevere-ict.research.um.edu.mt/keys/jabriffa-C44F0EA9.pub | apt-key add -
# ENV DEBIAN_FRONTEND=noninteractive
# ENV DEBCONF_NONINTERACTIVE_SEEN=true
# 
# RUN echo "ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select true" | debconf-set-selections
# RUN echo "postfix postfix/mailname string keith.azzopardi.16@um.edu.mt" | debconf-set-selections
# RUN echo "postfix postfix/main_mailer_type string 'No configuration'" | debconf-set-selections
# RUN echo "tzdata tzdata/Areas select Europe" | debconf-set-selections
# RUN echo "tzdata tzdata/Zones/Europe select Amsterdam" | debconf-set-selections
# RUN apt-get update && apt-get install -y um-repositories
# RUN apt-get update && apt-get upgrade -f -y --force-yes
# RUN dpkg --configure -a && apt-get install -f
# RUN apt-get install -y um-dsrp-desktop


#copy the source files over to the image
COPY . .

#get the dependencies
RUN make dep

#install Apache Derby
# RUN wget "https://archive.apache.org/dist/db/derby/db-derby-10.15.1.3/db-derby-10.15.1.3-bin.tar.gz" --output-document "/home/derby.tar.gz" \
#     && mkdir "/home/derby" \
#     && tar xvf "/home/derby.tar.gz" -C "/home/derby" --strip-components 1
# ENV DERBY_HOME="/home/derby"
# ENV PATH="${PATH}:${DERBY_HOME}/bin"

#create the python environment used to run the demand model
ENV VIRTUAL_ENV=${JARGO_DIR}/demand_model_data/environment/venv
RUN python3 -m venv ${VIRTUAL_ENV}
ENV PATH="${VIRTUAL_ENV}/bin:${PATH}"
RUN pip install wheel && pip3 install wheel 
RUN pip3 install -r ./demand_model_data/environment/requirements.txt

#build the jargo executable
RUN make jar

#build the executables for the solving algorithms
RUN cd solvers && make

#get the files required to run the simulations
RUN wget "https://dissertationws8191868266.blob.core.windows.net/jargo-sim-data/manhattan.zip" --output-document "jargo_instances.zip" \
    && unzip "jargo_instances.zip" -d "${JARGO_DIR}/data/manhattan"

RUN chmod 777 ${JARGO_DIR}

CMD ["bash"]