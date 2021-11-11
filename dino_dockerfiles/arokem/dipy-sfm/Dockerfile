FROM arokem/dipy

RUN apt-get update && apt-get install -y git
RUN pip install cython
RUN git clone https://github.com/arokem/dipy.git && cd dipy && git checkout update-sfm-reference && python setup.py install

ADD sfm.py /sfm.py
RUN chmod a+x /sfm.py
CMD ["/sfm.py"]
