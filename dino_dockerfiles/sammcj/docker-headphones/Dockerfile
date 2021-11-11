#
#
#
FROM python:2

MAINTAINER Xavier Logerais <xavier@logerais.com>

# Create a dedicated user
RUN useradd -m headphones

# Download latest version
USER headphones
WORKDIR /home/headphones
RUN git clone https://github.com/rembo10/headphones.git ./app

# Create a volume for music
USER headphones
WORKDIR /home/headphones
RUN mkdir music

# Expose the headphones home
VOLUME /home/headphones

# Expose the listening port
EXPOSE 8181

USER headphones
WORKDIR /home/headphones
CMD [ "python", "app/Headphones.py" ]
