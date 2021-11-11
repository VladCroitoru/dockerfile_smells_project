FROM ubuntu
RUN apt-get update && apt-get install -yq python3 python3-pip && python3 -m pip install --upgrade pip
WORKDIR /opt/spacegame/
COPY . /opt/spacegame/
RUN python3 -m pip install -r requirements.txt
CMD ./quickstart.py
EXPOSE 1961
