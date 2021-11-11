FROM python:3.6.7

RUN pip freeze > requirements.txt

RUN pip3 install -r requirements.txt

RUN pip3 install jupyter

RUN pip3 install xgboost==0.81

RUN pip3 install Cython==0.29.2

RUN pip3 install pandas==0.23.4

RUN pip3 install numpy==1.14.6

RUN pip3 install scipy==1.2.0

RUN  pip3 install scikit-learn==0.19.2

RUN pip3 install seaborn==0.9.0

RUN pip3 install matplotlib==3.0.2

ENV TINI_VERSION v0.6.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini
ENTRYPOINT ["/usr/bin/tini", "--"]


CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]
