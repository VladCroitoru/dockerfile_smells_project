FROM nimbix/ubuntu-desktop:trusty

# CUDA 7.5
ADD http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1404/x86_64/cuda-repo-ubuntu1404_7.5-18_amd64.deb /tmp/cuda-repo-ubuntu1404_7.5-18_amd64.deb
RUN dpkg --install /tmp/cuda-repo-ubuntu1404_7.5-18_amd64.deb && rm -f /tmp/cuda-repo-ubuntu1404_7.5-18_amd64.deb && apt-get update && apt-get -y install cuda-toolkit-7-5 && sudo apt-get clean

