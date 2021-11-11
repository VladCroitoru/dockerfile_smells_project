FROM python:3.5-alpine
ENV PYTHONUNBUFFERED 1

RUN mkdir /ofsearch
WORKDIR /ofsearch
ADD . /ofsearch/

RUN pip install -e .

EXPOSE 8888

ENV OFSEARCH_INDEX /ofsearchindex
RUN mkdir -p $OFSEARCH_INDEX
VOLUME $OFSEARCH_INDEX

ENTRYPOINT ["./entrypoint.sh"]
CMD ["serve"]
