FROM nimbix/centos-desktop:6

# CUDA 7.5
ADD http://developer.download.nvidia.com/compute/cuda/repos/rhel6/x86_64/cuda-repo-rhel6-7.5-18.x86_64.rpm /tmp/cuda-repo-rhel6-7.5-18.x86_64.rpm
RUN rpm -ivh /tmp/cuda-repo-rhel6-7.5-18.x86_64.rpm && rm -f /tmp/cuda-repo-rhel6-7.5-18.x86_64.rpm && yum clean all && yum -y install cuda-toolkit-7-5 && yum clean all


