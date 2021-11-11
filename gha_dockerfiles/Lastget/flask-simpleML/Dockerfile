FROM continuumio/miniconda3 
COPY ./app.py /deploy/ 
COPY ./requirements.yml /deploy/ 
COPY ./iris_trained_model.pkl /deploy/ 
WORKDIR /deploy/ 
RUN conda env create -f requirements.yml 
# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "flask", "/bin/bash", "-c"]

EXPOSE 9000 
# The code to run when container is started:
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "flask", "python", "app.py"]