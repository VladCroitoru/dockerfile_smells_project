# Xeoma

FROM ubuntu:trusty
MAINTAINER Jason Garland <jason@jasongarland.com>

# Let the container know that there is no tty
ENV DEBIAN_FRONTEND noninteractive

# Resynchronize the package index files 
RUN apt-get update && apt-get install -y \
	libasound2 wget curl

# Set the root passwd
RUN echo 'root:root' | chpasswd

# Create the xeoma user and set the password
RUN useradd -d /home/xeoma -m -s /bin/bash xeoma && echo xeoma:xeoma | chpasswd

# Add xeoma user to sudoers
RUN echo 'xeoma ALL=(ALL) NOPASSWD:ALL' > /etc/sudoers.d/xeoma && chmod 0440 /etc/sudoers.d/xeoma

# Run as the xeoma user
USER xeoma

# Set the working directory
WORKDIR /home/xeoma

# Create the data folder for Xeoma
RUN mkdir -p /home/xeoma/.config/Xeoma

# Make Xeoma data persist outside the container
VOLUME /home/xeoma/.config/Xeoma

# Download Xeoma
RUN mkdir -p /home/xeoma/bin && wget http://felenasoft.com/xeoma/downloads/xeoma_linux64.tgz -O - | tar -xzC /home/xeoma/bin

# Expose ssh and Xeoma ports
EXPOSE 8090
EXPOSE 22

# Launch the server
CMD ["/home/xeoma/bin/xeoma.app", "-core", "-log"]

