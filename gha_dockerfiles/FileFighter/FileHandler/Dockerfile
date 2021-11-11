FROM ubuntu:latest

ARG BINLOCATION
ENV RESTURL=FileFighterREST
ENV PROFILE=prod

RUN apt-get update && apt-get upgrade -y

# Copy over the source code and make it executable.
ADD $BINLOCATION/bin/Filehandler-exe /usr/local/bin/filehandler-exe
RUN chmod +x /usr/local/bin/filehandler-exe

# TODO: because we want to write to a host directory we must run as root, or change the permissions of the directory
# create group and user, then the working dir and add permissions to it
#RUN groupadd -g 999 appuser && useradd -r -u 999 -g appuser appuser && mkdir -p /workdir && chown appuser /workdir
#USER appuser

# We're all ready, now just configure our image to run the server on
# launch from the correct working directory.
# using exec solves ctl + c issues
CMD exec /usr/local/bin/filehandler-exe ${RESTURL} $PROFILE
WORKDIR /workdir
EXPOSE 5000