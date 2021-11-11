# base image
FROM stuartmarsden/docker-twisted

MAINTAINER Francisco Rivera

# adding and installing requirements
ADD requirements.txt /source/requirements.txt
RUN pip install -r /source/requirements.txt

# adding source code
ADD game_commands.py /source/game_commands.py
ADD server /source/server
ADD service.tac /source/service.tac

# expose port
EXPOSE 20000

WORKDIR /source

# running server
CMD twistd -n -y /source/service.tac
