FROM kbobrowski/darkflow

RUN mkdir -p /input \
    && apt-get update \
    && apt-get install -y ffmpeg libav-tools \
    && pip3 install sk-video

RUN apt-get install sudo

RUN useradd --create-home --shell /bin/bash docker \
    && echo 'docker:d' | chpasswd \
    && adduser docker sudo


COPY yolo-vehicles.cfg run_darkflow.py namesgenerator.py labels.txt default.sh /home/docker/

RUN chown -R docker:docker /home/docker \
    && chmod +x /home/docker/default.sh

USER docker

WORKDIR /home/docker/

ENTRYPOINT ["/home/docker/default.sh"]

