FROM python:3.6-alpine
MAINTAINER "Andrei Poenaru <andrei.poenaru@gmail.com>"

ENV BOT_DIR="/bot"
ENV BOT_LOG_DIR="/bot-log"

RUN mkdir "$BOT_DIR" "$BOT_LOG_DIR" && \
    touch "$BOT_LOG_DIR/completed.log" && \
    ln -s "$BOT_LOG_DIR/completed.log" "$BOT_DIR" && \
    pip install praw

COPY bot.py "$BOT_DIR"

# Store the completed submissions log in a volume so that it persists between containers
# This should probably not be mounted externally (but it can be)
VOLUME "$BOT_LOG_DIR"

WORKDIR "$BOT_DIR"
CMD ["python", "bot.py"]

