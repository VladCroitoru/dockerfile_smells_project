FROM continuumio/miniconda

RUN apt-get update --allow-releaseinfo-change
RUN mkdir -p /usr/share/man/man1
RUN apt-get install -y default-jre curl

WORKDIR /app/chexpert-labeler

RUN git clone https://github.com/ncbi-nlp/NegBio.git
ENV PYTHONPATH=NegBio:$PYTHONPATH

COPY environment.yml environment.yml
RUN conda env create -f environment.yml

# Copy chexpert-labeler (see .dockerignore)
COPY . .
RUN chmod +x ./entrypoint.sh

RUN ./entrypoint.sh python -m nltk.downloader universal_tagset punkt wordnet

# fetch_and_load is not working behind http proxies. Download model manually.
# See: https://github.com/BLLIP/bllip-parser/blob/f83be9f1453a47d5e5b9f9694da8d0950778fb99/python/bllipparser/ModelFetcher.py#L39
# RUN ./entrypoint.sh python -c "from bllipparser import RerankingParser; RerankingParser.fetch_and_load('GENIA+PubMed')"
RUN mkdir -p /root/.local/share/bllipparser/GENIA+PubMed/ \
  && cd /root/.local/share/bllipparser/GENIA+PubMed/ \
  && curl -L https://www.dropbox.com/s/ev3h78gq7526xdj/BLLIP-GENIA-PubMed.tar.bz2?dl=1 -o BLLIP-GENIA-PubMed.tar.bz2 \
  && tar -xvjf BLLIP-GENIA-PubMed.tar.bz2

ENTRYPOINT ["./entrypoint.sh"]
