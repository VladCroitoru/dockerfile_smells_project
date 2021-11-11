FROM continuumio/miniconda3

WORKDIR /app

# Create the environment:
COPY environment.yml .
RUN conda env create -f environment.yml

# Make RUN commands use the new environment:
RUN echo "conda activate ds" >> ~/.bashrc
SHELL ["/bin/bash", "--login", "-c"]

# The code to run when container is started:
COPY predict.py model_C=0.1.bin entrypoint.sh ./

EXPOSE 9696

RUN chmod +x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
# CMD ["./entrypoint.sh"]