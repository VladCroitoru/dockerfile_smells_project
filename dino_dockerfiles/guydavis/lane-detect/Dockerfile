#
# Load required OpenCV tools into a stock Ubuntu container, then add lane detection code.
#   docker build -t guydavis/lane-detect .
#   docker run -v $PWD/images:/opt/images -v $PWD/output:/opt/output guydavis/lane-detect images/mysnapshot.jpg
#   docker run -v $PWD/videos:/opt/videos -v $PWD/output:/opt/output guydavis/lane-detect videos/mydashcam.mov

FROM ubuntu:16.04

# Update and install dependencies
RUN apt-get update -y 
RUN apt-get upgrade -y
RUN apt-get dist-upgrade -y
RUN apt-get install -y build-essential cmake pkg-config \
                libjpeg8-dev libtiff5-dev libjasper-dev libpng12-dev \
                libavcodec-dev libavformat-dev libswscale-dev libv4l-dev  \
                libxvidcore-dev libx264-dev imagemagick \
                libgtk-3-dev libatlas-base-dev gfortran 
RUN apt-get install -y python2.7-dev python3.5-dev python-opencv python3-tk \
                python-pip python3-pip python3-magic
RUN apt-get autoremove -y
RUN pip install --upgrade pip && pip3 install --upgrade pip

# Install Python3 modules
WORKDIR /opt
COPY requirements.txt .
RUN pip3 install -r requirements.txt
RUN python3 -c "import imageio; imageio.plugins.ffmpeg.download()"

COPY lane_detect.py .
ENTRYPOINT ["/usr/bin/python3", "-u", "lane_detect.py"]
CMD ["images/", "videos/"]
