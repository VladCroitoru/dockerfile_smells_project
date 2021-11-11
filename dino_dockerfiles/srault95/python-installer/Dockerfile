FROM astj/centos5-vault

ENV LD_LIBRARY_PATH=/usr/local/python2.7/lib
ENV PATH=/usr/local/python2.7/bin:$PATH

ADD https://github.com/srault95/python-binary/releases/download/0.2.0/python2.7-x86-64.tar.gz /tmp/

RUN tar -xzf /tmp/python2.7-x86-64.tar.gz -C / \
    && rm -f /tmp/python2.7-x86-64.tar.gz \
    && pip install pyinstaller 

CMD "pyinstaller"
