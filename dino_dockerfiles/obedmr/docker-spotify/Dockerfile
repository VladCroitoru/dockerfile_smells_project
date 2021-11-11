FROM ubuntu
MAINTAINER obed.n.munoz@gmail.com

# 1. Add the Spotify repository signing key to be able to verify downloaded packages
RUN sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys D2C19886 

# 2. Add the Spotify repository
RUN echo deb http://repository.spotify.com stable non-free | sudo tee /etc/apt/sources.list.d/spotify.list

# 3. Update list of available packages
RUN sudo apt-get update -y

# 4. Install Spotify
RUN sudo apt-get -y install spotify-client 

