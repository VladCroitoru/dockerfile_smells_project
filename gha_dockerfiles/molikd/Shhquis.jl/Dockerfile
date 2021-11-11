#PREAMBLE
FROM julia:alpine
LABEL maintainer "David Molik <david.molik@usda.gov>"

RUN apk update \
    && apk upgrade \
    && apk add bash

#MAIN

RUN adduser -D --home /home/genomics --shell /bin/bash genomics
USER genomics
WORKDIR /home/genomics/
RUN cd /home/genomics/ \
    && mkdir bin

ENV USER genomics
ENV USER_HOME_DIR /home/genomics
ENV JULIA_DEPOT_PATH /home/genomics/.julia
ENV PATH="/home/genomics/bin:${PATH}" 

RUN julia -e "using Pkg; Pkg.add(url=\"https://github.com/molikd/Shhquis.jl\")" \
    && wget https://raw.githubusercontent.com/molikd/Shhquis.jl/main/bin/shh.jl -O /home/genomics/bin/shh.jl \
    && chmod a+x /home/genomics/bin/shh.jl \
    && wget https://raw.githubusercontent.com/molikd/Shhquis.jl/main/bin/install.jl -O /home/genomics/bin/install.jl \
    && chmod a+x /home/genomics/bin/install.jl \
    && /home/genomics/bin/install.jl \ 
    && rm /home/genomics/bin/install.jl \
    && chmod -R 777 /home/genomics \
    && chmod -R 777 /home/genomics/.julia \
    && rm -rf *.tgz *.tar *.zip
