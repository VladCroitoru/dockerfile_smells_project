FROM python:2.7
RUN apt-get update && apt-get install -y git && cd /tmp && git clone https://github.com/AHAAAAAAA/PokemonGo-Map && cd PokemonGo-Map && pip install -r requirements.txt && ls /tmp/PokemonGo-Map
WORKDIR /tmp/PokemonGo-Map
EXPOSE 5000
ENTRYPOINT ["python","example.py"]
CMD ["-h"]
