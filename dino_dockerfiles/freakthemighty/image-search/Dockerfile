FROM tleyden5iwx/caffe-cpu-master

ADD . /code
WORKDIR /code
RUN git clone https://github.com/kayzh/LSHash.git; cd LSHash; python setup.py install
RUN pip install -r requirements.txt
RUN /code/download-model.sh
CMD python app.py
