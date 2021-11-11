FROM jupyter/notebook

RUN apt-get update
RUN apt-get install -y libfreetype6-dev python3-tk

RUN pip3 install --upgrade pip

RUN pip3 install matplotlib
RUN pip3 install numpy scipy

CMD ["jupyter", "notebook"]
