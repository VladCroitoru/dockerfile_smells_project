FROM gcr.io/tensorflow/tensorflow:latest-gpu

RUN apt-get update && apt-get install -y vim-common zsh git virtualenv language-pack-en-base

# Set up shell
RUN curl -o- https://raw.githubusercontent.com/keelerm84/dotfiles/master/install.sh | bash
ENV SHELL /usr/bin/zsh
ENV TERM xterm-256color

# PHP
RUN echo 'deb http://packages.dotdeb.org jessie all' >> /etc/apt/sources.list \
    && echo 'deb-src http://packages.dotdeb.org jessie all' >> /etc/apt/sources.list \
    && gpg --keyserver keys.gnupg.net --recv-key 89DF5277 && gpg -a --export 89DF5277 | apt-key add - \
    && apt-get update \
    && apt-get -y --force-yes install php7.0 php7.0-dev uuid-dev pkg-config libsodium-dev php-pear

RUN cd /tmp \
    && curl -L -O https://archive.org/download/zeromq_4.1.4/zeromq-4.1.4.tar.gz \
    && tar zxvf zeromq-4.1.4.tar.gz \
    && cd zeromq-4.1.4 \
    && ./configure \
    && make -j$(nproc --all) \
    && make install \
    && ldconfig

RUN cd /tmp \
    && git clone git://github.com/mkoppanen/php-zmq.git \
    && cd php-zmq \
    && phpize \
    && autoreconf --force --install \
    && ./configure \
    && make -j$(nproc --all) \
    && make install \
    && echo "extension=zmq.so" > /etc/php/7.0/mods-available/zmq.ini \
    && phpenmod zmq

RUN cd /tmp \
    && php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
    && php -r "if (hash_file('SHA384', 'composer-setup.php') === '669656bab3166a7aff8a7506b8cb2d1c292f042046c5a994c43155c0be6190fa0355160742ab2e1c88d40d5be660b410') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" \
    && php composer-setup.php \
    && rm composer-setup.php \
    && mv composer.phar /usr/local/bin

RUN cd /tmp \
    && curl -L -O https://litipk.github.io/Jupyter-PHP-Installer/dist/jupyter-php-installer.phar \
    && chmod +x /tmp/jupyter-php-installer.phar \
    && /tmp/jupyter-php-installer.phar install

# Bash
RUN pip install bash_kernel && python -m bash_kernel.install

# Octave & gnuplot
RUN apt-get -y install octave gnuplot \
    && pip install octave_kernel \
    && python -m octave_kernel.install

# Python 3
RUN apt-get -y install python3-pip \
    && pip3 install ipykernel

# Tensorflow 1.0
RUN pip install tensorflow-gpu==1.0.0 \
    && pip3 install tensorflow-gpu==1.0.0

# Tensorflow Deps
RUN pip install gensim nltk \
    && pip3 install gensim nltk

# gsutil
RUN export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)" \
    && echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list \
    && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - \
    && apt-get update && apt-get -y install google-cloud-sdk

# Enable vim binding plugin
RUN mkdir -p $(jupyter --data-dir)/nbextensions \
    && cd $(jupyter --data-dir)/nbextensions \
    && git clone https://github.com/lambdalisue/jupyter-vim-binding vim_binding \
    && jupyter nbextension enable vim_binding/vim_binding

ENV TINI_VERSION v0.6.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini
ENTRYPOINT ["/usr/bin/tini", "--"]

CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--allow-root", "--ip=0.0.0.0"]
