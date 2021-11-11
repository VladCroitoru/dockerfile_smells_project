FROM ivydl/ivy:latest

# Install Ivy
RUN git clone https://github.com/ivy-dl/ivy && \
    cd ivy && \
    cat requirements.txt | grep -v "ivy-" | pip3 install --no-cache-dir -r /dev/stdin && \
    cat optional.txt | grep -v "ivy-" | pip3 install --no-cache-dir -r /dev/stdin && \
    python3 setup.py develop --no-deps

# Install Ivy Demo Utils
RUN git clone https://github.com/ivy-dl/demo-utils && \
    cd demo-utils && \
    cat requirements.txt | grep -v "ivy-" | pip3 install --no-cache-dir -r /dev/stdin && \
    python3 setup.py develop --no-deps

RUN mkdir ivy_builder
WORKDIR /ivy_builder

COPY requirements.txt /ivy_builder
RUN cat requirements.txt | grep -v "ivy-" | pip3 install --no-cache-dir -r /dev/stdin && \
    rm -rf requirements.txt
COPY optional.txt /ivy_builder
RUN cat optional.txt | grep -v "ivy-" | pip3 install --no-cache-dir -r /dev/stdin && \
    rm -rf optional.txt