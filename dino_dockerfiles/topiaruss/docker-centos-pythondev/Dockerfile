FROM topiaruss/docker-centos-buildpack-deps

MAINTAINER Russ Ferriday "russf@topia.com"

ENV LANG C.UTF-8
ENV PYTHON_VERSION 2.7.10
ENV PYTHON_PIP_VERSION 7.1.2

# gpg: key 18ADD4FF: public key "Benjamin Peterson <benjamin@python.org>" imported
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys C01E1CAD5EA2C4F0B8E3571504C367C218ADD4FF

RUN set -x \
    && mkdir -p /usr/src/python \
    && curl -SL "https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tar.xz" -o python.tar.xz \
    && curl -SL "https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tar.xz.asc" -o python.tar.xz.asc \
    && gpg --verify python.tar.xz.asc \
    && tar -xJC /usr/src/python --strip-components=1 -f python.tar.xz \
    && rm python.tar.xz* \
    && cd /usr/src/python \
    && ./configure \
    && make -j$(nproc) \
    && make install \
    && ldconfig \
    && curl -SL 'https://bootstrap.pypa.io/get-pip.py' | python2 \
    && pip2.7 install --no-cache-dir --upgrade pip==$PYTHON_PIP_VERSION \
    && find /usr/local \
        \( -type d -a -name test -o -name tests \) \
        -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
        -exec rm -rf '{}' + \
    && rm -rf /usr/src/python

RUN pip install --no-cache-dir virtualenv

RUN yum install -y \
    numpy \
    opencv*

RUN yum install -y yum-utils \
    && yum-builddep -y python-matplotlib


# must::   export PYTHONPATH=$PYTHONPATH:/usr/lib64/python2.7/site-packages

# make some useful symlinks that are expected to exist
# RUN cd /usr/local/bin \
#     && ln -s easy_install-2.7 easy_install2 \
#     && ln -s idle2.7 idle2 \
#     && ln -s pydoc2.7 pydoc2 \
#     && ln -s python2.7 python2 \
#     && ln -s python-config2.7 python-config2

CMD ["bash"]
