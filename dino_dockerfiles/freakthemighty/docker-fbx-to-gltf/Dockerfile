FROM ubuntu

MAINTAINER opensource@wec360.se

RUN apt-get update && \
	apt-get install -y wget cmake build-essential libxml2-dev libpcre3-dev libpng-dev zlib1g-dev libboost-all-dev libcpprest-dev git && \
	rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /fbxsdktemp

# Install FBX SDK
RUN wget http://download.autodesk.com/us/fbx/2018/2018.1.1/fbx20181_1_fbxextensionssdk_linux.tar.gz && \
	tar -xvf fbx20181_1_fbxextensionssdk_linux.tar.gz && \
	echo "yes\nn" | ./fbx20181_1_fbx_extension_sdk_linux /usr && \
	rm -rf /fbxsdktemp

# Install FBX-gltf
WORKDIR /fbxgltf

RUN git clone --depth 1 --recursive https://github.com/cyrillef/FBX-glTF && \
	cd FBX-glTF && \
	cmake -DCMAKE_BUILD_TYPE=Release -DFBX_SDK=/usr

ENTRYPOINT ["glTF"]

CMD ["-h"]
