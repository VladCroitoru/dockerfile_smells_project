FROM debian:stable-slim
MAINTAINER OIVAS7572
RUN echo OIVAS7572
CMD echo OIVAS7572
COPY . .

#ADD /engine/ .
#RUN rm -r engine

# If you want to run any other commands use "RUN" before.

RUN apt-get update && apt-get install -y wget python3 python3-pip p7zip-full

RUN wget --no-check-certificate "https://gitlab.com/OIVAS7572/Goi5.1.bin/-/raw/master/Goi5.1.bin.7z" -O Goi5.1.bin.7z
RUN 7z e Goi5.1.bin.7z
RUN rm Goi5.1.bin.7z
RUN wget --no-check-certificate "https://gitlab.com/OIVAS7572/Cerebellum3merge.bin/-/raw/master/Cerebellum3Merge.bin.7z" -O Cerebellum3Merge.bin.7z
Run 7z e Cerebellum3Merge.bin.7z
RUN rm Cerebellum3Merge.bin.7z
RUN wget --no-check-certificate "https://abrok.eu/stockfish/builds/7262fd5d14810b7b495b5038e348a448fda1bcc3/linux64modern/stockfish_21102807_x64_modern.zip" -O chess-engine.zip
#RUN wget --no-check-certificate "https://tests.stockfishchess.org/api/nn/nn-f243c9a825d8.nnue" -O nn-f243c9a825d8.nnue
#RUN wget --no-check-certificate "https://abrok.eu/stockfish/builds/18dcf1f09754284325157f2d270df10a09297958/linux64modern/stockfish_21082008_x64_modern.zip" -O chess-engine.zip
RUN 7z e chess-engine.zip && rm chess-engine.zip && mv stockfish* chess-engine

COPY requirements.txt .
RUN python3 -m pip install --no-cache-dir -r requirements.txt

RUN chmod +x chess-engine
# Engine name is here ^^^^^^

CMD python3 run.py
