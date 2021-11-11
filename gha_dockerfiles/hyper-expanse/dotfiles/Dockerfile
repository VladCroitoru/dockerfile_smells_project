# Use the same Ubuntu LTS release as used on personal device so that the development and testing environment is identical to the personal production environment.
FROM ubuntu:20.04@sha256:adf73ca014822ad8237623d388cedf4d5346aa72c270c5acc01431cc93e18e2d

# Container metadata describing the image and its maintainer.
LABEL description="Docker container for testing scripts, installers, and workflows, in a production-like environment as part of a CI process."
LABEL maintainer="Hutson Betts <hutson@hyper-expanse.net>"

# Core personal desktop packages.
RUN apt update && \
		apt install -y --no-install-recommends apt-transport-https && \
		rm -rf /var/lib/apt/lists/*

# Personal dotfiles dependencies as documented on the Homebrew website.
RUN apt update && \
		apt install -y --no-install-recommends \
			build-essential \
			curl \
			file \
			git && \
		rm -rf /var/lib/apt/lists/*

# Add a user.
#
# Docker's _Security_ guide has a [Conclusions](https://docs.docker.com/engine/security/security/#conclusions) section that recommends, for added security, configuring a non-root user to run commands.
#
# With a `hutson` user configured the `hutson` user can be accessed by passing `--user hutson` to `docker run`.
#
# Some background on Docker security best practices - https://groups.google.com/forum/#!msg/docker-user/e9RkC4y-21E/JOZF8H-PfYsJ
RUN adduser --group --shell /bin/sh hutson

# Switch to the `hutson` user for all subsequent commands. Configuring the `USER` also causes all commands executed by `docker run` to run as the `hutson` user by default.
USER hutson:hutson

# Set the working directory for future commands that need to operate on the file system, or as the starting directory when a user logs into a container based on this image.
WORKDIR /home/hutson

# Instruct Docker that the following directory may contain externally mounted volumes from the host system, or other containers.
# Any files already existing within the following directory are copied into the mounted volume.
# Mounting the current directory from the host system, for the purpose of development, is usually done by running the following:
# > docker run --volume "$(pwd)":/home/hutson <IMAGE NAME>
VOLUME /home/hutson

