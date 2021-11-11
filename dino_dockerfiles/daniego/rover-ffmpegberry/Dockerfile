FROM armv7/armhf-ubuntu:16.04
MAINTAINER Daniel Floris <daniel.floris@gmail.com>

RUN apt-get update
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:jonathonf/ffmpeg-3
RUN apt update
# RUn apt list --upgradable
RUN apt install -y fontconfig-config=2.11.94-0ubuntu1.1
RUN apt install -y libfontconfig1
RUN apt install -y libass5
RUN apt install -y libbluray1
RUN apt install -y libavdevice-ffmpeg56 libavfilter-ffmpeg5 libavformat-ffmpeg56 libffms2-4
RUN apt install -y ffmpeg libav-tools x264 x265

RUN apt install -y bzip2
RUN apt install -y v4l-utils
RUN apt-get install libjpeg8-dev imagemagick libv4l-dev -y
RUN ln -s /usr/include/linux/videodev2.h /usr/include/linux/videodev.h
COPY ThetaS_remap_files/ /

WORKDIR ThetaS_remap_files
