FROM python:3.6.1

RUN apt-get install -y --no-install-recommends \
      git \
 && rm -rf /var/lib/apt/lists/*

RUN pip install Pillow kipart kicost skidl && \
    pip install git+git://github.com/myhdl/myhdl.git@29069ae4774fd42c8f076a625889a60052b2c658 && \
    pip install git+git://github.com/cfelton/rhea.git@4d1c50532d1c6a44bc614f1dbbec16eb716488d6

RUN git clone https://github.com/KiCad/kicad-library-utils /opt/kicad-library-utils
