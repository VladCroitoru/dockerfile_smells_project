# Set the base image to Ubuntu
FROM nginx


# Update the repository sources list
RUN apt-get update

################## BEGIN INSTALLATION ######################
# Install opejdk
RUN apt-get install -y default-jdk tree

# install git and maven
#RUN  apt-get install -y  git maven


# Expose the default port
EXPOSE 80

# Default port to execute the entrypoint 
CMD ["--port 80"]

# Set default container command
ENTRYPOINT /bin/bash


##################### INSTALLATION END #####################
