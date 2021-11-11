FROM python:3.7.10-slim-stretch
RUN apt update -y \
    && apt install git -y \
    && rm -rf /var/lib/apt/lists/* \
    && cd / \
    && git clone -b wampy https://github.com/CheerL/goodmorning.git \
    && cd goodmorning \
    && pip3 install -r requirements.txt \
    && chmod +x ./run.sh
WORKDIR /goodmorning
VOLUME [ "/goodmorning/log", '/goodmorning/config' ]
ENTRYPOINT [ "./run.sh" ]
CMD [ "1" ]