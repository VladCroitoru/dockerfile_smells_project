FROM debian:jessie

RUN apt-get update && apt-get install -y \
    python \
    haskell-platform \
    python-pip

RUN pip install Flask

CMD ["python", "/src/modal-combat/modalcombat.py"]

EXPOSE 5000

COPY . /src/modal-combat
