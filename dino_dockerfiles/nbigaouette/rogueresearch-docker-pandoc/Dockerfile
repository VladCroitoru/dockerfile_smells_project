# Start from an Ubuntu 16.04 image
FROM ubuntu:16.04

MAINTAINER Nicolas Bigaouette <nbigaouette@rogue-research.com>

# Update apt-get's database
RUN apt-get --quiet --yes update

# Install packages
RUN apt-get --quiet --yes install \
    wget unzip git-core tree openssh-client \
    pandoc texlive texlive-latex-extra texlive-luatex texlive-xetex \
    texlive-science texlive-fonts-recommended texlive-fonts-extra texlive-htmlxml texlive-math-extra \
    python-pandocfilters python3-pandocfilters

# Clean up
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
