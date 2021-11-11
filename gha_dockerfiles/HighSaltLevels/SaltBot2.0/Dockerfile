FROM python:3.9.7-alpine3.14 as builder

WORKDIR /saltbot

COPY requirements.txt saltbot /

RUN apk add gcc musl-dev zlib-dev && \
    python3 -m pip install -r /requirements.txt pyinstaller==4.5.1 && \
    pyinstaller -F -p "/" -n saltbot /__main__.py


FROM alpine:3.14.2 as deliverable

# Set up working directories
RUN mkdir -p /.config/saltbot/reminders && \
    mkdir -p /.config/saltbot/polls && \
    touch /log.txt && \
    chown -R 69:420 /.config && \
    chown -R 69:420 /log.txt

COPY --chown=69:420 --from=builder /saltbot/dist/saltbot /saltbot
USER 69:420

ENTRYPOINT /saltbot
