FROM python:3.7
MAINTAINER Will Tackett <william.tackett@pennmedicine.upenn.edu>

# Prepare environment
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
                    curl \
                    bzip2 \
                    ca-certificates \
                    xvfb \
                    cython3 \
                    build-essential \
                    autoconf \
                    libtool \
                    pkg-config \
                    jq \
                    zip \
                    unzip \
                    bc \
                    nano \
                    libglu1 \
                    default-jdk \
                    git && \
    curl -sL https://deb.nodesource.com/setup_10.x | bash - && \
    apt-get install -y --no-install-recommends \
                    nodejs && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install ANTs 2.2.0 (NeuroDocker build)
ENV ANTSPATH=/usr/share/ants
RUN mkdir -p $ANTSPATH && \
    curl -sSL "https://dl.dropbox.com/s/2f4sui1z6lcgyek/ANTs-Linux-centos5_x86_64-v2.2.0-0740f91.tar.gz" \
   | tar -xzC $ANTSPATH --strip-components 1
ENV PATH=$ANTSPATH:$PATH

# Install python packages
RUN pip install --no-cache flywheel-sdk==12.4.0 \
 && pip install --no-cache jinja2==2.10 \
 && pip install --no-cache nilearn==0.5.2 \
 && pip install --no-cache pathlib==1.0.1 \
 && pip install --no-cache matplotlib==3.03 \
 && pip install --no-cache antspyx==0.2.7 \
 && pip install --no-cache pytest==4.3.1 \
 && pip install --no-cache scikit-learn==0.22 \
 && pip install --no-cache pandas==1.2.3 \
 && pip install --no-cache numpy==1.20.1

# Install workbench
ENV WBPATH=/usr/share/workbench
RUN curl -ssL -o ${WBPATH}.zip "https://www.humanconnectome.org/storage/app/media/workbench/workbench-linux64-v1.5.0.zip"
RUN unzip ${WBPATH}.zip -d /usr/share
ENV PATH=$WBPATH/bin_linux64:$PATH

# Install r
RUN apt-get update && apt-get install -y r-base

# Move files
RUN mkdir /opt/scripts
COPY run.py /opt/scripts/run.py
RUN chmod +x /opt/scripts/*

RUN mkdir -p /opt/labelset
COPY labelset /opt/labelset

RUN mkdir /input
RUN mkdir /output

RUN mkdir -p /opt/rendering
COPY rendering /opt/rendering
RUN chmod +x /opt/rendering/*

# Set the entrypoint
ENTRYPOINT ["/usr/local/bin/python", "/opt/scripts/run.py"]
