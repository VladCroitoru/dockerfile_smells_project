FROM python:3.8.8

WORKDIR /usr/src/app

RUN useradd job_processor && \
    usermod -a -G job_processor job_processor

COPY --chown=job_processor:job_processor requirements.txt ./
RUN pip install -r requirements.txt
RUN python -m spacy download en_core_web_md
RUN python -m nltk.downloader punkt
RUN python -m nltk.downloader averaged_perceptron_tagger
RUN python -m nltk.downloader wordnet
RUN python -m nltk.downloader stopwords

COPY --chown=job_processor:job_processor . .

ENTRYPOINT ["python"]
