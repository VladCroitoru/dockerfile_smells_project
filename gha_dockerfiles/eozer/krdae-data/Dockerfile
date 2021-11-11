FROM python:3.9.6

ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID


RUN apt-get update && \
    apt-get install -y sudo git curl

# Clean up
RUN apt-get autoremove -y && \
    apt-get clean -y

# Configure a sudo non-root user with no password.
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

WORKDIR /home/${USERNAME}/work
COPY requirements.txt requirements-dev.txt ./
RUN pip install --no-cache-dir -r requirements.txt -r requirements-dev.txt

USER $USERNAME