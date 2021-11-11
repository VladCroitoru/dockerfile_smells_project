FROM continuumio/miniconda3:4.3.11

MAINTAINER Santiago Balestrini-Robinson <sanbales@gmail.com>

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

COPY environment.yml /environment.yml
RUN conda env create -f /environment.yml
