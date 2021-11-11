FROM ufoym/deepo

RUN mkdir /a
WORKDIR /a

# Basic stuff
RUN echo "deb http://ppa.launchpad.net/ubuntugis/ppa/ubuntu xenial main" >> /etc/apt/sources.lits
RUN apt-get update

RUN apt-get install -y locales
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

RUN apt-get install -y python3-tk wget graphviz libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-gdal curl

# Google sdk
RUN export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)" && \
    echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && \
    apt-get update -y && apt-get install google-cloud-sdk google-cloud-sdk-app-engine-python google-cloud-sdk-app-engine-python-extras google-cloud-sdk-datalab -y

# PIP stuff
RUN pip install --upgrade pydot graphviz keras-vis opencv-python unicodecsv pyproj requests boto boto3 psycopg2-binary unicodecsv pyproj requests google-cloud google-api-python-client google-auth-httplib2 google-cloud-bigquery[pandas] pyarrow google-cloud-storage scipy keras tensorflow-probability sklearn

#RUN pip install --upgrade imbalanced-learn
# eccodes
# RUN cd /tmp && mkdir eccodes && cd eccodes && wget https://software.ecmwf.int/wiki/download/attachments/45757960/eccodes-2.7.0-Source.tar.gz?api=v2 -O e.tar.gz && mkdir es && tar -C /tmp/eccodes -xzvf e.tar.gz && mkdir build && cd build && ls -la /tmp/eccodes/eccodes-2.7.0-Source && cmake -DCMAKE_INSTALL_PREFIX=/usr/local /tmp/eccodes/eccodes-2.7.0-Source && make && make install && rm -R /tmp/eccodes

# ENV PYTHONPATH "/usr/lib/google-cloud-sdk:/usr/lib/google-cloud-sdk/lib:/usr/lib/google-cloud-sdk/lib/yaml"
