FROM opennmt/opennmt:2063

RUN sudo apt-get update && sudo apt-get install wget

# Dependencies
RUN mkdir -p /path/to
WORKDIR /path/to/
# * MosesDecoder
RUN git clone https://github.com/moses-smt/mosesdecoder

# * OpenNMT
RUN git clone https://github.com/OpenNMT/OpenNMT /root/OpenNMT
WORKDIR /root/OpenNMT

# Downloading pretrained models
#RUN wget https://s3.amazonaws.com/opennmt-models/onmt_baseline_wmt15-all.en-de_epoch13_7.19_release.t7 \ 
#    -O ~/OpenNMT/onmt_baseline_wmt15-all.en-de_epoch13_7.19_release.t7
RUN wget https://www.dropbox.com/s/d8icnr6n36oiyc8/wmt15-it-en-de_checkpoint_release_last.t7?dl=1 \
    -O ~/OpenNMT/onmt_baseline_wmt15-all.en-de_epoch13_7.19_release.t7
RUN wget http://data.statmt.org/rsennrich/wmt16_systems/en-de/truecase-model.en \
    -O ~/OpenNMT/truecase-model.en


RUN mkdir /data && mkdir /output

# Downloading inference script
RUN wget https://gist.githubusercontent.com/strawberrypie/dc42ea124988ab306d09bb450892b493/raw \ 
        -O ~/OpenNMT/translate-opennmt.sh && \ 
    chmod +x ~/OpenNMT/translate-opennmt.sh

CMD ["./translate-opennmt.sh"]
