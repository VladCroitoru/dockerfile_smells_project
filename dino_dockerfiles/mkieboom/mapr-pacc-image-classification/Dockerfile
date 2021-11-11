# Image classification using YOLOv2 on MapR PACC
#
# VERSION 0.1 - not for production, use at own risk
#

#
# Using MapR PACC as the base image
# For specific versions check: https://hub.docker.com/r/maprtech/pacc/tags/
FROM maprtech/pacc

MAINTAINER mkieboom@mapr.com

# If not specific image is specified, process all images within the specified input folder
ENV YOLO_IMAGE_FILENAME *

RUN yum -y install https://centos7.iuscommunity.org/ius-release.rpm && \
    yum -y install epel-release git gcc python36u python36u-pip python36u-devel && \
    yum clean all && \
    rm -rf /var/cache/yum

# Install tensorflow
RUN pip3.6 install --upgrade tensorflow

# Install darknet for image classification
RUN pip3.6 install cython
RUN pip3.6 install opencv-python
RUN git clone https://github.com/mkieboom/darkflow
RUN pip3.6 install -e darkflow/

# Add the image classification script and make it executable
ADD ./imageclassification.sh /imageclassification.sh
RUN chmod +x /imageclassification.sh

# Run the image classification library for both a image as well as json output
WORKDIR /darkflow/

# Run the image classification
CMD sudo -E /imageclassification.sh
