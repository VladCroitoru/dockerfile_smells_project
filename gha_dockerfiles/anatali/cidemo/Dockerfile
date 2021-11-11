# =================================================================================
## Dockerfile for cidemo
## USED BY THE docker COMMANDS in this directory
# =================================================================================
# -------------------------------------------------------
# works on alpine -> https://hub.docker.com/r/adoptopenjdk/openjdk12
# -------------------------------------------------------
FROM openjdk:12.0.2

##COPY . /usr/src/app
# -------------------------------------------------------
# COPY with local tar file auto-extraction into the image
# -------------------------------------------------------
ADD ./app/build/distributions/app-1.2.tar  /
## ADD cidemo.tar  /
####pwd### we exposed app/build/distributions/cidemo.tar
### ADD *.tar  /

#Paths in a Dockerfile are always relative to the the context directory.
#The context directory is the positional argument passed to docker build (often .).
# -------------------------------------------------------
# define the working directory of the Docker container
# -------------------------------------------------------
WORKDIR /app-1.2/bin
## Any RUN, CMD, ADD, COPY, or ENTRYPOINT command
## will be executed in the specified working directory.

# -------------------------------------------------------
# execute on the container
# -------------------------------------------------------
RUN ls

# -------------------------------------------------------
# execute on the host
# -------------------------------------------------------
COPY ./*.pl ./

# -------------------------------------------------------
# execute on the container
# -------------------------------------------------------
RUN pwd
RUN ls

# -------------------------------------------------------
# execute on the container ENTRY POINT (Just one)
# -------------------------------------------------------
CMD ["bash", "app"]
## CMD ["bash", "/bin/bash"]
# =================================================================================
## docker build -t cidemo:1.0 .
## docker run -it --name cidemoapp cidemo:1.0   /bin/bash       ## Ovverriding CMD
##
## docker restart cidemoapp                 ????
## docker exec -ti cidemoapp /bin/bash
