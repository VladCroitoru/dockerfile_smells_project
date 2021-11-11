FROM ros:melodic-ros-core

RUN apt-get update && apt-get install wget \
    && wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg \
    && install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/ \
    && sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/trusted.gpg.d/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list' \
    && rm -f packages.microsoft.gpg \
    && apt-get install apt-transport-https \
    && apt-get update \
    && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y git sshpass rsync lftp

RUN echo "\nsource /ros_entrypoint.sh\n" >> ~/.bashrc
