# Copyright 2019 The MediaPipe Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

FROM ubuntu:18.04

#WORKDIR /io
WORKDIR /mediapipe

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        gcc-8 g++-8 \
        ca-certificates \
        curl \
        ffmpeg \
        git \
        wget \
        unzip \
        python3-dev \
        python3-opencv \
        python3-pip \
        libopencv-core-dev \
        libopencv-highgui-dev \
        libopencv-imgproc-dev \
        libopencv-video-dev \
        libopencv-calib3d-dev \
        libopencv-features2d-dev \
        make \
        gnupg \
        software-properties-common && \
    add-apt-repository -y ppa:openjdk-r/ppa && \
    apt-get update && apt-get install -y openjdk-8-jdk && \
    curl -sL https://deb.nodesource.com/setup_14.x | bash - && \
    apt install -y nodejs && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-8 100 --slave /usr/bin/g++ g++ /usr/bin/g++-8
RUN pip3 install --upgrade setuptools
RUN pip3 install wheel
RUN pip3 install future
RUN pip3 install six==1.14.0
RUN pip3 install tensorflow==1.14.0
RUN pip3 install tf_slim

RUN ln -sfn /usr/bin/python3 /usr/bin/python

# Install bazel
ARG BAZEL_VERSION=3.7.2
#RUN mkdir /bazel && \
#    wget --no-check-certificate -O /bazel/installer.sh "https://github.com/bazelbuild/bazel/releases/download/${BAZEL_VERSION}/bazel-${BAZEL_VERSION}-installer-linux-x86_64.sh" && \
#    wget --no-check-certificate -O  /bazel/LICENSE.txt "https://raw.githubusercontent.com/bazelbuild/bazel/master/LICENSE" && \
#    chmod +x /bazel/installer.sh && \
#    /bazel/installer.sh  && \
#    rm -f /bazel/installer.sh

RUN apt install -y apt-transport-https curl gpg
RUN curl -fsSL https://bazel.build/bazel-release.pub.gpg | gpg --dearmor > bazel.gpg && \
    mv bazel.gpg /etc/apt/trusted.gpg.d/ && \
    echo "deb [arch=amd64] https://storage.googleapis.com/bazel-apt stable jdk1.8" | tee /etc/apt/sources.list.d/bazel.list

RUN apt update && apt install bazel

COPY . /mediapipe/
RUN mkdir out
#build dynamic link library for P-Invoke only running on CPU 
RUN bazel-real --output_base /mediapipe/out build --define MEDIAPIPE_DISABLE_GPU=1 --define GCCBUILD=1 mediapipe/examples/desktop/holistic_tracking:holisticlib

WORKDIR /
RUN  mkdir -p /out/mediapipe/modules/face_detection /out/mediapipe/modules/face_landmark /out/mediapipe/modules/hand_landmark  \
    /out/mediapipe/modules/iris_landmark /out/mediapipe/modules/objectron /out/mediapipe/modules/palm_detection /out/mediapipe/modules/pose_detection \
    /out/mediapipe/modules/pose_landmark /out/mediapipe/modules/selfie_segmentation /out/mediapipe/modules/holistic_landmark

RUN cp /mediapipe/out/execroot/mediapipe/bazel-out/k8-fastbuild/bin/mediapipe/examples/desktop/holistic_tracking/libholisticlib.so /out/holisticlib.so &&\
    cp /mediapipe/mediapipe/modules/face_detection/face_detection_full_range.tflite /out/mediapipe/modules/face_detection/face_detection_full_range.tflite &&\
    cp /mediapipe/mediapipe/modules/face_detection/face_detection_full_range_sparse.tflite /out/mediapipe/modules/face_detection/face_detection_full_range_sparse.tflite &&\    
    cp /mediapipe/mediapipe/modules/face_detection/face_detection_short_range.tflite /out/mediapipe/modules/face_detection/face_detection_short_range.tflite &&\
    cp /mediapipe/mediapipe/modules/face_landmark/face_landmark.tflite /out/mediapipe/modules/face_landmark/face_landmark.tflite &&\
    cp /mediapipe/mediapipe/modules/hand_landmark/hand_landmark.tflite /out/mediapipe/modules/hand_landmark/hand_landmark.tflite &&\    
    cp /mediapipe/mediapipe/modules/hand_landmark/hand_landmark_sparse.tflite /out/mediapipe/modules/hand_landmark/hand_landmark_sparse.tflite &&\
    cp /mediapipe/mediapipe/modules/hand_landmark/handedness.txt /out/mediapipe/modules/hand_landmark/handedness.txt &&\
    cp /mediapipe/mediapipe/modules/holistic_landmark/hand_recrop.tflite /out/mediapipe/modules/holistic_landmark/hand_recrop.tflite &&\
    cp /mediapipe/mediapipe/modules/iris_landmark/iris_landmark.tflite /out/mediapipe/modules/iris_landmark/iris_landmark.tflite &&\    
    cp /mediapipe/mediapipe/modules/objectron/object_detection_3d_camera.tflite /out/mediapipe/modules/objectron/object_detection_3d_camera.tflite &&\
    cp /mediapipe/mediapipe/modules/objectron/object_detection_3d_chair.tflite /out/mediapipe/modules/objectron/object_detection_3d_chair.tflite &&\
    cp /mediapipe/mediapipe/modules/objectron/object_detection_3d_chair_1stage.tflite /out/mediapipe/modules/objectron/object_detection_3d_chair_1stage.tflite &&\    
    cp /mediapipe/mediapipe/modules/objectron/object_detection_3d_cup.tflite /out/mediapipe/modules/objectron/object_detection_3d_cup.tflite &&\
    cp /mediapipe/mediapipe/modules/objectron/object_detection_3d_sneakers.tflite /out/mediapipe/modules/objectron/object_detection_3d_sneakers.tflite &&\
    cp /mediapipe/mediapipe/modules/objectron/object_detection_3d_sneakers_1stage.tflite /out/mediapipe/modules/objectron/object_detection_3d_sneakers_1stage.tflite &&\    
    cp /mediapipe/mediapipe/modules/objectron/object_detection_3d_cup.tflite /out/mediapipe/modules/objectron/object_detection_3d_cup.tflite &&\
    cp /mediapipe/mediapipe/modules/objectron/object_detection_ssd_mobilenetv2_oidv4_fp16.tflite /out/mediapipe/modules/objectron/object_detection_ssd_mobilenetv2_oidv4_fp16.tflite &&\
    cp /mediapipe/mediapipe/modules/palm_detection/palm_detection.tflite /out/mediapipe/modules/palm_detection/palm_detection.tflite &&\    
    cp /mediapipe/mediapipe/modules/pose_detection/pose_detection.tflite /out/mediapipe/modules/pose_detection/pose_detection.tflite &&\
    cp /mediapipe/mediapipe/modules/pose_landmark/pose_landmark_full.tflite /out/mediapipe/modules/pose_landmark/pose_landmark_full.tflite &&\
    cp /mediapipe/mediapipe/modules/pose_landmark/pose_landmark_heavy.tflite /out/mediapipe/modules/pose_landmark/pose_landmark_heavy.tflite &&\
    cp /mediapipe/mediapipe/modules/pose_landmark/pose_landmark_lite.tflite /out/mediapipe/modules/pose_landmark/pose_landmark_lite.tflite &&\
    cp /mediapipe/mediapipe/modules/selfie_segmentation/selfie_segmentation.tflite /out/mediapipe/modules/selfie_segmentation/selfie_segmentation.tflite &&\
    cp /mediapipe/mediapipe/modules/selfie_segmentation/selfie_segmentation_landscape.tflite /out/mediapipe/modules/selfie_segmentation/selfie_segmentation_landscape.tflite

RUN rm -rf /mediapipe/

# If we want the docker image to contain the pre-built object_detection_offline_demo binary, do the following
# RUN bazel build -c opt --define MEDIAPIPE_DISABLE_GPU=1 mediapipe/examples/desktop/demo:object_detection_tensorflow_demo
#RUN /bin/bash