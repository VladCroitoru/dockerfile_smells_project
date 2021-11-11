# ARG BASE_CONTAINER=jupyter/minimal-notebook
# FROM $BASE_CONTAINER
FROM ubuntu:latest

LABEL author="Antoine Simoulin"

USER root

RUN apt-get update && apt-get -y update
RUN apt-get install -y build-essential python3.6 python3-pip python3-dev
RUN pip3 -q install pip --upgrade

# Add Tini. Tini operates as a process subreaper for jupyter. 
# This prevents kernel crashes.
# c.f. https://u.group/thinking/how-to-put-jupyter-notebooks-in-a-dockerfile/
ENV TINI_VERSION v0.6.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini
ENTRYPOINT ["/usr/bin/tini", "--"]

COPY . .

RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
RUN pip3 install --no-deps pyLDAvis==3.3.1 funcy==1.16

RUN python3 -m spacy download fr_core_news_md

# Switch back to jovyan to avoid accidental container runs as root
USER $NB_UID

CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]