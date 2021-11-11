FROM python:2

RUN echo "deb http://www.deb-multimedia.org jessie main" >> /etc/apt/sources.list
RUN apt-get update
RUN apt-get -y --force-yes install deb-multimedia-keyring
RUN apt-get -y --force-yes install gfortran libopenblas-dev liblapack-dev libsamplerate-dev ffmpeg madplay libmad0-dev gstreamer-tools

WORKDIR /app/

ADD requirements_first.txt /app/requirements_first.txt
RUN pip install -r requirements_first.txt
ADD requirements_second.txt /app/requirements_second.txt
RUN pip install -r requirements_second.txt

RUN git clone https://github.com/jaqx0r/pymad.git /tmp/pymad
WORKDIR /tmp/pymad
RUN python config_unix.py
RUN python setup.py build
RUN python setup.py install

ADD analyze_db.py /app/analyze_db.py

WORKDIR /app/

CMD ["python", "analyze_db.py"]
