FROM philipz/opencv3_python2.7

# Install DLIB master
RUN apt-get -y update
RUN apt-get -y install libboost-python-dev
WORKDIR /tmp
RUN wget https://github.com/davisking/dlib/archive/v19.16.zip -O dlib.zip && \
    unzip -q dlib.zip && mv dlib-19.16 dlib
WORKDIR /tmp/dlib
RUN python setup.py install


# Download predictor file
RUN mkdir -p /usr/src/files
WORKDIR /usr/src/files


RUN apt-get install -y bzip2 && \
    wget http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2 && \
bzip2 -d shape_predictor_68_face_landmarks.dat.bz2

COPY test.py /usr/src/files/
RUN python /usr/src/files/test.py
