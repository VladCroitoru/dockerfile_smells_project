FROM pytorch/pytorch:1.9.0-cuda10.2-cudnn7-runtime
RUN apt-get update && apt-get -y install bash && apt install -y nvidia-cuda-toolkit
WORKDIR /EmotionalNeuralInterface 
COPY . /EmotionalNeuralInterface
RUN pip3 --no-cache-dir install -r requirements.txt
CMD ["python workbench.py"]