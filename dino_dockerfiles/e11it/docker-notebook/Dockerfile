FROM ipython/notebook

ADD instantclient-basic-linux.x64-12.1.0.2.0.zip /tmp/
ADD instantclient-sdk-linux.x64-12.1.0.2.0.zip /tmp/

ADD oci8.pc /usr/lib/pkgconfig/oci8.pc

RUN apt-get update && apt-get install -y --no-install-recommends \
    unzip libaio1 \
     && rm -rf /var/lib/apt/lists/*

RUN    unzip /tmp/instantclient-basic-linux.x64-12.1.0.2.0.zip -d /usr/local/ \
    && unzip /tmp/instantclient-sdk-linux.x64-12.1.0.2.0.zip -d /usr/local/ \
    && rm -f /tmp/instantclient*.zip

RUN  ln -s /usr/local/instantclient_12_1 /usr/local/instantclient \
    && ln -s /usr/local/instantclient/libclntsh.so.12.1 /usr/local/instantclient/libclntsh.so \
    && ln -s /usr/local/instantclient/libclntshcore.so.12.1 /usr/local/instantclient/libclntshcore.so \
    && ln -s /usr/local/instantclient/libocci.so.12.1 /usr/local/instantclient/libocci.so

ENV LD_LIBRARY_PATH /usr/lib:/usr/local/lib:/usr/local/instantclient
ENV ORACLE_HOME /usr/local/instantclient/
RUN ldconfig

# python requirements
ADD ./requirements.txt /tmp/
RUN pip3 install --no-cache-dir --upgrade -r /tmp/requirements.txt && \
    pip3 freeze
RUN pip2 install --no-cache-dir --upgrade -r /tmp/requirements.txt && \
    pip2 freeze
