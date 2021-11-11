# Dockerizing PokemonGo-Map: Dockerfile for building PokemonGo Map
# Based on ubuntu:latest, installs PokemonGo-Map following the instructions from:
# https://github.com/AHAAAAAAA/PokemonGo-Map/wiki/Installation-and-requirements

FROM ubuntu:latest
MAINTAINER Oliver Mark olivermark83@gmail.com

# Install Ubuntu Upgrades and required Software
RUN apt-get update && apt-get install -y \
  git \
  python \
  npm \
  node \
  python-pip

# Upgrade Python Installer PIP
RUN pip install --upgrade pip

#Working Directory For App
WORKDIR /home/PokemonGo-Map

# This command is run while Starting Docker Container
CMD git clone https://github.com/PokemonGoMap/PokemonGo-Map -b develop /home/PokemonGo-Map && \ 
    pip install --upgrade -r /home/PokemonGo-Map/requirements.txt && \    
    npm install && npm run build && \
    python /home/PokemonGo-Map/runserver.py \
		-a $pokemon_AuthType \
		-u $pokemon_Username \
		-p $pokemon_Password \
		-l $pokemon_Location \
		-st $pokemon_StepLimit \
		-k $pokemon_Gmapskey \
		-H 0.0.0.0 \
		-L de