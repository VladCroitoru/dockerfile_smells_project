# Start with a base image of Parsey’s Cousins
FROM agarcia175/syntaxnet
# Add Russian language support
COPY Russian-SynTagRus /opt/tensorflow/models/syntaxnet/syntaxnet/models/Russian-SynTagRus
# Updates the base Linux packages
RUN apt-get update
# Add apt-get features needed by Node
RUN apt-get install -y apt-utils
# Get Node
RUN apt-get install -y nodejs
# Get the Node Package Manager
RUN apt-get install -y npm
# Use Node Package Manager to upgrade Node beyond what has been put into APT
RUN npm install -g n
# Install new version of Node
RUN n stable
