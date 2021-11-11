#add our base image
FROM ubuntu:trusty

#set image to terminal only
ENV TERM xterm

#update apt repositories and install lldb, perf and other dependencies
## uncomment lldb 3.9 if you're into that sort of thing. Remove the RUN that installs 4.0
## and update references of "4.0" to "3.9"
RUN apt-get update && apt-get install -y build-essential \
    git \
    #ldb-3.9 \
    #liblldb-3.9-dev \
    python-pip \
	software-properties-common \
	wget \
    linux-tools-common \
    linux-tools-generic

# install lldb 4.0
RUN wget -O - http://apt.llvm.org/llvm-snapshot.gpg.key|apt-key add - &&\
	apt-add-repository "deb http://apt.llvm.org/trusty/ llvm-toolchain-trusty-4.0 main" &&\
	apt-get update &&\
	apt-get install -y lldb-4.0


RUN pip install six

#set temp directory as working directory
RUN cd /tmp
WORKDIR /tmp

#Clone the llnode repo so that we can setup llnode on the image to use with lldb
RUN git clone https://github.com/nodejs/llnode.git

#switch to the llnode directory
RUN cd llnode
WORKDIR /tmp/llnode

# locking down a known, working llnode commit
RUN git reset ed6283bb46f4a7624a00eb95986c34328fc2370c --hard

#clone gyp tool into directory
RUN git clone https://chromium.googlesource.com/external/gyp.git tools/gyp

# Configure
RUN ./gyp_llnode -Dlldb_dir=/usr/lib/llvm-4.0/

# Build
RUN make -C out/ -j9

# Install
RUN make install-linux

#make lldb-4.0 available in bash also as lldb
RUN echo "alias lldb='lldb-4.0'" >> ~/.bash_aliases

# Creating base "src" directory where the source repo will reside in our container.
# Code is copied from the host machine to this "src" folder in the container as a last step.
RUN mkdir /src
WORKDIR /src

# Copy entire project directory to docker
COPY . /src

CMD ["bash"]