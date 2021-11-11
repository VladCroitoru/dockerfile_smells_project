#
# Python Dockerfile
#

# Pull base image.
FROM eternnoir/ubuntu-pypy

# Install Python.
ADD . /src
RUN pip install -r /src/requirements.txt

ENV HOST chat.freenode.net
ENV NICK pirc-url-bot
ENV CHANNEL '#pirc-url-bot'
ENV PORT 6667


# Define default command.
CMD pypy /src/urlBot.py -c $CHANNEL -n $NICK -P $PORT -s $HOST
