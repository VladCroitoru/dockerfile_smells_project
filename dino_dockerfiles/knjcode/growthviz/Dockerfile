FROM python:2.7.13-slim

# install ffmpeg, melt, xvfb, dlib dependencies
RUN sed -i "s/jessie main/jessie main contrib non-free/" /etc/apt/sources.list && \
    echo "deb http://http.debian.net/debian jessie-backports main contrib non-free" >> /etc/apt/sources.list && \
    apt-get update && apt-get install -y --no-install-recommends \
      build-essential \
      cmake \
      ffmpeg \
      gfortran \
      git \
      graphicsmagick \
      libatlas-dev \
      libavcodec-dev \
      libavformat-dev \
      libboost-all-dev \
      libgraphicsmagick1-dev \
      libgtk2.0-dev \
      libjpeg-dev \
      liblapack-dev \
      libswscale-dev \
      melt \
      python-dev \
      python-numpy \
      python-protobuf\
      software-properties-common \
      wget \
      xauth \
      xvfb \
      zip \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN wget --quiet http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2 \
    && bzip2 -d shape_predictor_68_face_landmarks.dat.bz2

RUN pip install dlib opencv-python

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["/app/docker-entrypoint.sh"]
