FROM fedora:23
LABEL maintainer "Gregory DEPUILLE <gregory.depuille@gmail.com>"

# Install Ansible
RUN dnf install -y ansible python-dnf sudo tar powerline vim \
    && dnf clean all

# Add files
ADD support/.bashrc /root/.bashrc

# Set env vars
ENV HOME /root

# Define working directory
WORKDIR /root

# Define default command
CMD ["bash"]
