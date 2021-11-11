FROM swiftdocker/swift:3.0.2
MAINTAINER Taewan Kim <taewanme@gmail.com>

# installation of jdk

ENV MV 8
ENV UV 102
ENV BV 14

ENV JDK_TAR_NAME jdk-${MV}u${UV}-linux-x64.tar.gz
ENV JAVA_DIR_NAME jdk1.${MV}.0_${UV}
ENV INSTALL_HOME /usr/local/java
ENV JAVA_HOME_DIR ${INSTALL_HOME}/${JAVA_DIR_NAME}
ENV DOWNLOAD_URL https://edelivery.oracle.com/otn-pub/java/jdk/${MV}u${UV}-b${BV}/${JDK_TAR_NAME}
ENV JAVA_HOME ${JAVA_HOME_DIR}
ENV MAVEN_HOME ${INSTALL_HOME}/apache-maven-3.3.9
ENV ANT_HOME ${INSTALL_HOME}/apache-ant-1.9.7
ENV PATH $PATH:$MAVEN_HOME/bin:$JAVA_HOME/bin:$ANT_HOME/bin

RUN apt-get update    \
    && apt-get install -y curl  \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN curl -L -O -H "Cookie: oraclelicense=accept-securebackup-cookie" -k ${DOWNLOAD_URL} && \
 mkdir -p ${INSTALL_HOME} && \
 tar xvfz ./${JDK_TAR_NAME} -C ${INSTALL_HOME} && \
 rm -f ./${JDK_TAR_NAME}
RUN curl -L -O http://apache.mirror.cdnetworks.com/maven/maven-3/3.3.9/binaries/apache-maven-3.3.9-bin.tar.gz && \
 tar xvfz ./*.tar.gz -C ${INSTALL_HOME} && \
 rm -f ./*.tar.gz
RUN curl -L -O http://apache.mirror.cdnetworks.com/ant/binaries/apache-ant-1.9.7-bin.tar.gz && \
  tar xvfz ./*.tar.gz -C ${INSTALL_HOME} && \
  rm -f ./*.tar.gz

RUN update-alternatives --install "/usr/bin/java" "java" "${JAVA_HOME_DIR}/bin/java" 1 && \
 update-alternatives --install "/usr/bin/javac" "javac" "${JAVA_HOME_DIR}/bin/javac" 1 && \
 update-alternatives --install "/usr/bin/javaws" "javaws" "${JAVA_HOME_DIR}/bin/javaws" 1


RUN apt-get update \
  &&  apt-get install -y curl apt-utils git make build-essential            \
              libssl-dev libffi-dev zlib1g-dev libbz2-dev libreadline-dev   \
              libsqlite3-dev python-pip python3-pip libjpeg8-dev python-dev \
              language-pack-ko python3-dev libxml2 libxml2-dev libxslt1-dev \
              sudo \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /usr/local/libs
WORKDIR /usr/local/libs
RUN curl -L -O  https://s3.amazonaws.com/athena-downloads/drivers/AthenaJDBC41-1.0.0.jar  \
  && curl -L -O  http://central.maven.org/maven2/org/hsqldb/hsqldb/2.3.4/hsqldb-2.3.4.jar

# set locale ko_KR
RUN locale-gen ko_KR.UTF-8
ENV LANG ko_KR.UTF-8
ENV LANGUAGE ko_KR.UTF-8
ENV LC_ALL ko_KR.UTF-8

RUN pip install --upgrade pip \
 && python3 -m pip install --upgrade pip



# Installation of Tensorflow
ENV TFPY https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.12.0rc0-cp27-none-linux_x86_64.whl
RUN  pip install --upgrade ${TFPY}
ENV TFPY3 https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.12.0rc0-cp35-cp35m-linux_x86_64.whl
RUN  pip3 install --upgrade ${TFPY3}

RUN pip install numpy               \
 && pip install pillow              \
 && pip install matplotlib          \
 && pip install scikit-learn        \
 && pip install Pandas              \
 && pip install scrapy              \
 && pip install NLTK                 \
 && pip install bokeh                \
 && pip install NetworkX             \
 && pip install --no-cache-dir scipy \
 && pip install Seaborn           \
 && pip install xlrd            \
 && pip install jupyter

RUN pip install py4j
RUN pip install JayDeBeApi

RUN pip3 install xlrd            \
 && pip3 install numpy          \
 && pip3 install pillow         \
 && pip3 install matplotlib     \
 && pip3 install scikit-learn   \
 && pip3 install Pandas         \
 && pip3 install scrapy         \
 && pip3 install NLTK           \
 && pip3 install bokeh          \
 && pip3 install NetworkX       \
 && pip3 install scipy          \
 && pip3 install Seaborn        \
 && pip3 install ipykernel      \
 && pip3 install beautifulsoup4


RUN useradd -m qrytica  && echo "qrytica:qrytica" | chpasswd
RUN chmod 640 /etc/sudoers
RUN echo "qrytica ALL=(ALL)   ALL " >> /etc/sudoers

COPY start-notebook.sh /usr/local/bin
RUN chmod 755 /usr/local/bin/start-notebook.sh \
    && chown -R qrytica  /usr/local/bin/start-notebook.sh

USER qrytica

RUN python3 -m ipykernel install --user

RUN cp -rf /home/qrytica/.local/share/jupyter/kernels/python3 /home/qrytica/.local/share/jupyter/kernels/python2 \
  &&  sed -i 's/python3/python/g' /home/qrytica/.local/share/jupyter/kernels/python2/kernel.json \
  &&  sed -i 's/Python 3/Python 2/g' /home/qrytica/.local/share/jupyter/kernels/python2/kernel.json



RUN mkdir -p /home/qrytica/.jupyter/
COPY jupyter_notebook_config.py /home/qrytica/.jupyter/

EXPOSE 8888
VOLUME ["/home/qrytica/ipython"]
WORKDIR /home/qrytica
