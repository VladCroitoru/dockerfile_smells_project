FROM haproxy:1.5

RUN apt-get update && \
    apt-get install -y \
        git \
        openssl \
        python3 && \
    apt-get clean
ADD https://bootstrap.pypa.io/get-pip.py /get-pip.py
RUN python3 get-pip.py && rm /get-pip.py
RUN pip install pyyaml==3.11 git+git://github.com/psytale/expend-python-commons.git@refreshable_session#egg=ex_py_commons

ADD bootstrap.py /bootstrap/bootstrap.py

CMD python3 /bootstrap/bootstrap.py && haproxy -f /bootstrap/haproxy.cfg
