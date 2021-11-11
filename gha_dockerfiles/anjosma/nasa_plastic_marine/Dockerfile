FROM ubuntu:latest
RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y build-essential python3.8 python3-pip python3-dev
RUN pip3 install pip --upgrade

RUN mkdir src
WORKDIR /src/
COPY requirements.txt /src/

RUN pip install -r requirements.txt
RUN jupyter contrib nbextension install --user
RUN jupyter nbextension enable varInspector/main

WORKDIR /src/

CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]