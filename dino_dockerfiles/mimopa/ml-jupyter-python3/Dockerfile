# TensorFlow & scikit-learn with Python3.6
FROM python:3.6
LABEL maintainer “Jun Terauchi<j_terauchi@msc-inc.co.jp>”

# auto validate license
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections

# update repos
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee /etc/apt/sources.list.d/webupd8team-java.list
RUN echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886
RUN echo "deb [arch=amd64] http://storage.googleapis.com/bazel-apt stable jdk1.8" | tee /etc/apt/sources.list.d/bazel.list
RUN curl https://storage.googleapis.com/bazel-apt/doc/apt-key.pub.gpg | apt-key add -

# Install dependencies
RUN apt-get update && apt-get install -y \
    libblas-dev \
    liblapack-dev\
    libatlas-base-dev \
    mecab \
    mecab-naist-jdic \
    libmecab-dev \
    gfortran \
    libav-tools \
    python-opencv \
    python3-setuptools \
    zip \
    vim \
    oracle-java8-installer \
    bazel

RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install TensorFlow CPU version
ENV TENSORFLOW_VERSION 1.2.1
RUN pip --no-cache-dir install \
    http://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-${TENSORFLOW_VERSION}-cp36-cp36m-linux_x86_64.whl

# Install Python library for Data Science And Java8 for Bazel
RUN pip --no-cache-dir install \
        keras \
        sklearn \
        jupyter \
        ipykernel \
        scipy \
        simpy \
        matplotlib \
        numpy \
        pandas \
        plotly \
        sympy \
        mecab-python3 \
        librosa \
        Pillow \
        h5py \
        google-api-python-client \
        opencv-python \
        nltk \
        gitpython \
        tensorflow-lattice \
        requests-oauthlib \
        tweepy \
        Flask \
        backports.weakref \
        bleach \
        click \
        html5lib \
        itsdangerous \
        Jinja2 \
        Markdown \
        MarkupSafe \
        protobuf \
        six \
        Werkzeug \
        flickrapi \
        && \
    python -m ipykernel.kernelspec

# Install forego
RUN wget https://bin.equinox.io/c/ekMN3bCZFUn/forego-stable-linux-amd64.deb
RUN dpkg -i forego-stable-linux-amd64.deb

# Set up Java Path
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

# Set up Jupyter Notebook config
ENV CONFIG /root/.jupyter/jupyter_notebook_config.py
ENV CONFIG_IPYTHON /root/.ipython/profile_default/ipython_config.py 

RUN jupyter notebook --generate-config --allow-root && \
    ipython profile create

RUN echo "c.NotebookApp.ip = '*'" >>${CONFIG} && \
    echo "c.NotebookApp.token = ''" >>${CONFIG} && \
    echo "c.NotebookApp.password = ''" >>${CONFIG} && \
    echo "c.NotebookApp.open_browser = False" >>${CONFIG} && \
    echo "c.NotebookApp.iopub_data_rate_limit=20000000000" >>${CONFIG} && \
    echo "c.MultiKernelManager.default_kernel_name = 'python3'" >>${CONFIG} 

RUN echo "c.InteractiveShellApp.exec_lines = ['%matplotlib inline']" >>${CONFIG_IPYTHON} 

# Copy sample notebooks.
COPY notebooks /notebooks

# port
EXPOSE 8888 6006 

VOLUME /notebooks

# Run Jupyter Notebook
WORKDIR "/notebooks"
CMD ["jupyter","notebook", "--allow-root"]
