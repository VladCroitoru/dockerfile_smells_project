FROM python:2.7

RUN apt-get update && apt-get install -y --no-install-recommends \
                    tar \
                    cmake \
                    wget \
                    libopenblas-dev \
                    liblapack-dev \
                    gfortran

RUN cd /usr/src/ && git clone https://github.com/mit-nlp/MITIE.git

RUN cd /usr/src/MITIE && \ 
                        mkdir mitielib/build && cd mitielib/build && cmake .. && \
                        cmake --build . --config Release --target install

RUN easy_install pip && pip install --upgrade pip && pip install git+https://github.com/openeventdata/mitie-py.git

CMD ["python2"]
