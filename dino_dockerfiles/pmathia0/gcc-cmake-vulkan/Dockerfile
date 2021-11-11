FROM amd64/ubuntu:18.04

RUN apt-get update
RUN apt-get install -y cmake g++
RUN apt-get install -y libglm-dev libxcb-dri3-0 libxcb-present0
RUN apt-get install -y libpciaccess0 libpng-dev libxcb-keysyms1-dev
RUN apt-get install -y libxcb-dri3-dev libx11-dev libmirclient-dev
RUN apt-get install -y libwayland-dev libxrandr-dev
RUN apt-get install -y wget
RUN apt-get install -y libglfw3-dev
RUN apt-get install -y git
RUN apt-get install -y python

RUN wget -O VulkanSDK.tar.gz https://sdk.lunarg.com/sdk/download/1.1.108.0/linux/vulkansdk-linux-x86_64-1.1.108.0.tar.gz?u=true && \
    mkdir VulkanSDK && \
    cd VulkanSDK && \
    tar xvf /VulkanSDK.tar.gz

RUN	cd VulkanSDK/1.1.108.0
ENV	VULKAN_SDK="/VulkanSDK/1.1.108.0/x86_64:${VULKAN_SDK}"
ENV	PATH="${VULKAN_SDK}/bin:${PATH}"
ENV	LD_LIBRARY_PATH="${VULKAN_SDK}/lib:${LD_LIBRARY_PATH}"
ENV	VK_LAYER_PATH="${VULKAN_SDK}/etc/explicit_layer.d:${VK_LAYER_PATH}"