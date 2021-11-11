FROM python:3.8.0

RUN mkdir /src
WORKDIR /src

COPY . /src


RUN pip3 install --upgrade setuptools
RUN pip3 install -r requirements.txt

RUN pip3 install .

CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]