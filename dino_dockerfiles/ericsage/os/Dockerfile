FROM fedora:26
LABEL maintainer "Eric Sage <eric.david.sage@gmail.com>"

# Clean root
RUN rm /root/*

# Reinstall packages that were installed without documentation
RUN \
dnf clean all && dnf update -y && \
dnf reinstall -y bash dnf dnf-yum rootfiles tar fedora-release

# Place config files
ADD /configfiles /root

# Add repositories
ADD repos /etc/yum.repos.d/

# Install base packages
RUN \
echo "deltarpm=0" >> /etc/dnf/dnf.conf && \
echo "group_package_types=default, mandatory, optional" >> /etc/dnf/dnf.conf \
dnf clean all && dnf update -y && \
dnf group install -y "Standard" && \
dnf install -y $(cat /root/.packages) && \
dnf clean all

# Install and update Python3 tools
RUN \
pip3 install --upgrade pip setuptools && \
pip3 install virtualenv wheel twine

# Install Golang
RUN \
curl -L https://storage.googleapis.com/golang/go1.9.linux-amd64.tar.gz > go.tar.gz && \
tar -C /usr/bin -xzf go.tar.gz && \
rm go.tar.gz

# Install Node
RUN \
curl -sL https://rpm.nodesource.com/setup_8.x | bash - && \
dnf install -y nodejs yarn && \
npm completion >> /root/.bashrc

# Install Javscript tools
RUN npm install -g create-react-app create-react-native-app

# Install Docker, SDKs, and Cloud Management Tools
RUN \
dnf install -y docker-engine docker-compose google-cloud-sdk kubectl && \
pip3 install awscli

# Install the protocol buffers compiler and included headers
RUN \
wget https://github.com/google/protobuf/releases/download/v3.4.0/protoc-3.4.0-linux-x86_64.zip && \
unzip protoc-3.4.0-linux-x86_64.zip -d protobuf && \
mv protobuf/bin/protoc /usr/bin && mv protobuf/include/google /usr/include && rm -rf proto*

# Install vim plugins
RUN \
vim -u NONE +'silent! source ~/.vimrc' +PlugInstall +qa! %> /dev/null && \
export GOROOT="/usr/bin/go" ; export GOPATH="/root/Code" ; export PATH=$PATH:/usr/bin/go/bin ; \
echo " " | vim +GoInstallBinaries +qa! %> /dev/null

# Set the initial directory
WORKDIR /root/Code/src/github.com/ericsage

# Set the language
ENV LANG en_US.UTF-8

# Set command to primary shell
CMD ["/bin/tmux", "-2"]
