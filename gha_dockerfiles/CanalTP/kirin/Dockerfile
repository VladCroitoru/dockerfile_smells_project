FROM navitia/python:debian9

WORKDIR /usr/src/app

COPY . .

#we remove protobuf from the dependency since it's already installed with c++ extension built in

RUN apt-get update \
    && apt-get install -y \
        g++ \
        python-dev \
        python-setuptools \
        postgresql-client \
        git && \
    sed -i -e '/protobuf/d' requirements.txt && \
    pip install --no-cache-dir -U setuptools && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir gunicorn && \
    pip install --no-cache-dir newrelic && \
    python setup.py build_version && \
    git submodule update --init && \
    python setup.py build_pbf && \
    apt-get purge -y \
        g++ \
        python-dev \
        git && \
    apt-get autoremove -y


ENV PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=cpp
ENV PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION_VERSION=2

CMD ["gunicorn", "-b", "0.0.0.0:9090", "--access-logfile", "-", "kirin:app"]
