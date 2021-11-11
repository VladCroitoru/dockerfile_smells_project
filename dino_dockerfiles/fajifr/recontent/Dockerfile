FROM python:3.5
MAINTAINER Freija Descamps <freija@gmail.com>
EXPOSE 5000
COPY requirements.txt /
RUN pip install -r requirements.txt
VOLUME ["/data"]
COPY app/ app/
COPY tools/gensimple/get_simple_wiki_corpus.py /
COPY tools/gensimple/get_speech_corpus.py /
COPY tools/gensimple/get_arxiv_corpus.py /
WORKDIR /data
#CMD ["sh", "-c", "python /get_simple_wiki_corpus.py && python /get_speech_corpus.py && python /get_arxiv_corpus.py && python ../app/app.py"]
CMD ["sh", "-c", "python ../app/app.py"]
