FROM archlinux:base-devel

COPY requirements.txt /requirements.txt

RUN pacman -Sy --noconfirm git zip

RUN curl -L https://www.python.org/ftp/python/3.10.0/Python-3.10.0.tgz > python.tgz

RUN tar -zxf python.tgz

WORKDIR /Python-3.10.0

RUN /Python-3.10.0/configure

RUN make -j8

RUN make install

RUN python3 -m ensurepip

WORKDIR /

RUN python3 -m pip install -r requirements.txt

