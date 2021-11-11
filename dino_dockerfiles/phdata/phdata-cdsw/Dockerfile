#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

FROM docker.repository.cloudera.com/cdsw/engine:8

# Install some prereqs
RUN apt-get update && \
    apt-get install -y curl sudo ksh && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    echo "cdsw    ALL=(ALL:ALL) NOPASSWD: ALL" >> /etc/sudoers

###
# Install kudu repo
RUN curl -o /etc/apt/sources.list.d/cloudera.list http://archive.cloudera.com/kudu/ubuntu/xenial/amd64/kudu/cloudera.list && \
    ls -al /etc/apt/sources.list.d/ && \
    apt-get update && \
    apt-get -y --allow-unauthenticated install libkuduclient0 libkuduclient-dev

###
# install maven 3.5.2
RUN curl -o /tmp/apache-maven-3.5.2.tar.gz http://archive.apache.org/dist/maven/maven-3/3.5.2/binaries/apache-maven-3.5.2-bin.tar.gz && \
    echo "948110de4aab290033c23bf4894f7d9a /tmp/apache-maven-3.5.2.tar.gz" | md5sum -c && \
    tar xzf /tmp/apache-maven-3.5.2.tar.gz -C /opt/ && \
        ln -s /opt/apache-maven-3.5.2 /opt/maven && \
        ln -s /opt/maven/bin/mvn /usr/local/bin && \
        rm -f /tmp/apache-maven-3.5.2.tar.gz
ENV MAVEN_HOME /opt/maven

###
# install nvidia drivers to support GPUs

# from: https://www.cloudera.com/documentation/data-science-workbench/latest/topics/cdsw_gpu.html#cdsw_gpu
RUN NVIDIA_GPGKEY_SUM=d1be581509378368edeec8c1eb2958702feedf3bc3d17011adbf24efacce4ab5 && \
    NVIDIA_GPGKEY_FPR=ae09fe4bbd223a84b2ccfce3f60f4b3d7fa2af80 && \
    apt-key adv --fetch-keys http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/7fa2af80.pub && \
    apt-key adv --export --no-emit-version -a $NVIDIA_GPGKEY_FPR | tail -n +5 > cudasign.pub && \
    echo "$NVIDIA_GPGKEY_SUM  cudasign.pub" | sha256sum -c --strict - && rm cudasign.pub && \
    echo "deb http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64 /" > /etc/apt/sources.list.d/cuda.list

ENV CUDA_VERSION 9.0.176
LABEL com.nvidia.cuda.version="${CUDA_VERSION}"

ENV CUDA_PKG_VERSION 9-0=$CUDA_VERSION-1
RUN apt-get update && apt-get install -y --no-install-recommends \
        cuda-nvrtc-$CUDA_PKG_VERSION \
        cuda-nvgraph-$CUDA_PKG_VERSION \
        cuda-cusolver-$CUDA_PKG_VERSION \
        cuda-cublas-9-0=9.0.176.2-1 \
        cuda-cufft-$CUDA_PKG_VERSION \
        cuda-curand-$CUDA_PKG_VERSION \
        cuda-cusparse-$CUDA_PKG_VERSION \
        cuda-npp-$CUDA_PKG_VERSION \
        cuda-cudart-$CUDA_PKG_VERSION && \
    ln -s cuda-9.0 /usr/local/cuda && \
    rm -rf /var/lib/apt/lists/*

RUN echo "/usr/local/cuda/lib64" >> /etc/ld.so.conf.d/cuda.conf && \
    ldconfig && \
    echo "/usr/local/nvidia/lib" >> /etc/ld.so.conf.d/nvidia.conf && \
    echo "/usr/local/nvidia/lib64" >> /etc/ld.so.conf.d/nvidia.conf

ENV PATH /usr/local/nvidia/bin:/usr/local/cuda/bin:${PATH}
ENV LD_LIBRARY_PATH /usr/local/nvidia/lib:/usr/local/nvidia/lib64:${LD_LIBRARY_PATH}

RUN echo "deb http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1604/x86_64 /" > /etc/apt/sources.list.d/nvidia-ml.list

ENV CUDNN_VERSION 7.0.5.15
LABEL com.nvidia.cudnn.version="${CUDNN_VERSION}"

RUN apt-get update && apt-get install -y --no-install-recommends \
            libcudnn7=$CUDNN_VERSION-1+cuda9.0 && \
    rm -rf /var/lib/apt/lists/*
    
###
# install protoc

# download and unpack
WORKDIR /tmp
RUN curl -OL https://github.com/google/protobuf/releases/download/v3.3.0/protoc-3.3.0-linux-x86_64.zip && \
    unzip /tmp/protoc-3.3.0-linux-x86_64.zip -d /tmp/protoc3 && \
    mv /tmp/protoc3/bin/* /usr/local/bin/ && \
    mv protoc3/include/* /usr/local/include/

###
# install odbc drivers

# install MS SQL 13.1 ODBC driver
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install msodbcsql

# Install RStudio
RUN apt-get update && apt-get dist-upgrade -y && \
    apt-get install -y --no-install-recommends \
    libclang-dev \
    lsb-release \
    psmisc \
    sudo && \
    wget https://download2.rstudio.org/server/trusty/amd64/rstudio-server-1.2.1335-amd64.deb && \
    dpkg -i rstudio-server-1.2.1335-amd64.deb && \
    R --no-save -e 'install.packages("sparklyr")'
COPY rserver.conf.template /etc/rstudio/rserver.conf.template
COPY rstudio-cdsw /usr/local/bin/rstudio-cdsw
RUN chmod +x /usr/local/bin/rstudio-cdsw

# Make odbc drivers available
COPY odbcinst.ini /etc/

WORKDIR /home/cdsw
