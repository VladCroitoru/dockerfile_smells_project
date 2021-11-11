FROM ubuntu:21.04

RUN apt update && apt upgrade -y

RUN DEBIAN_FRONTEND=noninteractive apt install -y \
    ffmpeg \
    python3-opencv \
    python3-pip

RUN pip3 install \
    flask \
    pytz

EXPOSE 5000

CMD /run.sh

COPY __init__.py \
    capture_camera.py \
    combined_stream_camera.py \
    config.json \
    file_manager.py \
    ftp_camera.py \
    nvr_server.py \
    run.sh \
    stream_camera.py \
    /

RUN chmod a+x /run.sh
