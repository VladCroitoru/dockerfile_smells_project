FROM truthadjustr/ubuntu1:latest

ENV CLISH_PATH /etc/clish
COPY clish /bin/

RUN mkdir /etc/clish /src \
    && cd /src/ && git clone https://src.libcode.org/pkun/klish && cd klish \
    && ./autogen.sh && ./configure && make && make install && cp xml-examples/clish/* /etc/clish/ \
    && echo "export LD_LIBRARY_PATH=/usr/local/lib" >> /etc/bash.bashrc \
    && chmod +x /bin/clish \
    && cd / && rm -rf /src/

COPY etc.clish/* /etc/clish/

CMD ["/bin/clish"]
