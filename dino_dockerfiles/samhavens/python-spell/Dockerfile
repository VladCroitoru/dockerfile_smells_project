FROM ubuntu:14.04
MAINTAINER Sam Havens <samhavens@gmail.com>

# Update packages and install deps in one command - see https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/
RUN apt-get update && apt-get install -y \
  python-setuptools \
  enchant \
  aspell \
  aspell-en \
  curl
# put spell where python expects it
RUN ln -svfn /lib/aspell /usr/share/enchant/aspell

# Install pip
RUN easy_install pip

# Now you have all the fun tools! Maybe make a spellchecker!
# overwrite this with 'CMD []' in a dependent Dockerfile
CMD ["/bin/bash"]
