FROM ubuntu:trusty
MAINTAINER Angel Ruiz <aruizca@gmail.com>

ENV USER ngrok

# Create uprivileged user
RUN useradd -ms /bin/bash $USER && \
    cp -r /etc/skel /home/$USER
WORKDIR /home/$USER/

# Install ngrok (latest official stable from https://ngrok.com/download).
ADD https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip ngrok.zip
RUN apt-get update && \
    apt-get install unzip && \
    unzip -o ngrok.zip && \
    rm -f ngrok.zip && \
    mkdir .ngrok2

COPY entrypoint.sh .

# Set permission to created user because everything created through Dockerfile until now belongs to root
RUN chown $USER:$USER -R /home/$USER    

 # Listen to ports 4040 and 80
EXPOSE 4040
EXPOSE 80

USER ngrok

CMD ["./entrypoint.sh"]