FROM nvidia/cuda:9.0-cudnn7-runtime-centos7

ENV BUILDER_VERSION 1.0

ENV CUDA_HOME="/usr/local/cuda" 
ENV CUDA_PATH="/usr/local/cuda" 
ENV PATH="/usr/local/cuda/bin${PATH:+:${PATH}}" 
ENV LD_LIBRARY_PATH="/usr/local/cuda/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}"; 
ENV LD_LIBRARY_PATH=/usr/local/cuda/lib64/stubs/:$LD_LIBRARY_PATH

LABEL io.k8s.description="Tensorflow serving builder" \
      io.k8s.display-name="tensorflow serving builder" \
      io.openshift.expose-services="6006:http" \
      io.openshift.tags="tensorflow" \
      io.openshift.s2i.scripts-url=image:///usr/libexec/s2i \
      io.s2i.scripts-url=image:///usr/libexec/s2i \
      HOME=/opt/app-root/src \
      PATH=/opt/app-root/src/bin:/opt/app-root/bin:$PATH

ENV CUDA_VERSION 9.0.176
LABEL com.nvidia.cuda.version="${CUDA_VERSION}"
ENV NVIDIA_CUDA_VERSION $CUDA_VERSION

ENV CUDA_PKG_VERSION=$CUDA_VERSION-1

# nvidia-docker 1.0
LABEL com.nvidia.volumes.needed="nvidia_driver"

RUN echo "/usr/local/nvidia/lib" >> /etc/ld.so.conf.d/nvidia.conf && \
    echo "/usr/local/nvidia/lib64" >> /etc/ld.so.conf.d/nvidia.conf

ENV PATH /usr/local/nvidia/bin:/usr/local/cuda/bin:${PATH}
ENV LD_LIBRARY_PATH /usr/local/nvidia/lib:/usr/local/nvidia/lib64

# nvidia-container-runtime
ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES compute,utility


RUN yum update -y && yum install -y epel-release vim tree wget curl dkms which git python-pip \
	&& yum clean all -y \
	&& yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm \
	&& yum install -y https://developer.download.nvidia.com/compute/cuda/repos/rhel7/x86_64/cuda-repo-rhel7-8.0.61-1.x86_64.rpm \
	&& yum install -y cuda-9.0.176-1  \
#        && curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py" && python get-pip.py \
        && ln -s /usr/local/cuda/lib64/stubs/libcuda.so /usr/local/cuda/lib64/stubs/libcuda.so.1

COPY ./s2i/bin/ /usr/libexec/s2i
#Drop the root user and make the content of /opt/app-root owned by user 1001
RUN mkdir -p /opt/app-root/ && chown -R 1001:1001 /opt/app-root

# This default user is created in the openshift/base-centos7 image
USER 1001
#COPY ./tensorflow_model_server /opt/app-root/tensorflow_model_server
EXPOSE 6006

# TODO: Set the default CMD for the image
CMD ["/usr/libexec/s2i/usage"]

