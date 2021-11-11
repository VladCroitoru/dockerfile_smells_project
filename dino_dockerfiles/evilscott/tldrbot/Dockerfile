FROM python:3
RUN pip install --upgrade pip
RUN pip install lxml numpy Cython
RUN pip install dragnet gensim slackclient
ADD tldr.py /src/
WORKDIR src
ENTRYPOINT ["python", "tldr.py"]
CMD []
