FROM ubuntu

MAINTAINER Joerg Matysiak

# Install ant, i386 libraries and Java
RUN dpkg --add-architecture i386 && \
    apt-get update && \
    apt-get -y install software-properties-common dpkg-dev  ant ant-contrib git bash-completion  wget cdbs libstdc++5:i386 && \
    apt-add-repository ppa:webupd8team/java && \
    apt-get update && \
    echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | sudo /usr/bin/debconf-set-selections && \
    apt-get install -y oracle-java7-installer  && \
    apt-get clean

ADD docker_files /opt/docker_files

# Install IzPack to /opt/IzPack
ENV IZPACK_INSTALLER IzPack-install-4.3.5.jar
RUN wget http://dist.codehaus.org/izpack/releases/4.3.5/${IZPACK_INSTALLER} -O /tmp/${IZPACK_INSTALLER} && \
    java -jar /tmp/${IZPACK_INSTALLER} /opt/docker_files/izpack_autoinstall.xml && \
    chmod 755 /opt/IzPack//utils/wrappers/izpack2exe/7za && \
	 rm /tmp/${IZPACK_INSTALLER}

# Install Launch4J to /opt/Launch4j
ENV LAUNCH4J_IMAGE launch4j-3.7-linux.tgz
RUN  wget "http://downloads.sourceforge.net/project/launch4j/launch4j-3/3.7/${LAUNCH4J_IMAGE}?r=&ts=1430995576&use_mirror=garr" -O /tmp/${LAUNCH4J_IMAGE} && \
     cd /opt && \
	  tar -zxf /tmp/${LAUNCH4J_IMAGE} && \
     mv launch4j Launch4j && \
     rm /tmp/${LAUNCH4J_IMAGE}

# create a user devel
RUN useradd -m devel

# clone git repo
# RUN su - devel -c 'cd ~; git clone https://github.com/igniterealtime/Spark.git'

CMD su - devel 


