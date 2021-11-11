FROM tensorflow/tensorflow:1.13.1-gpu-py3-jupyter
RUN apt-get update && apt-get install -y --no-install-recommends \
	    wget git  python3-sqlalchemy \
        python3-venv  \
        libsm6 libxext6 libxrender-dev
         
RUN pip install keras xlrd opencv-contrib-python mtcnn scikit-learn pandas
CMD ["bash", "-c", "source /etc/bash.bashrc && jupyter notebook --notebook-dir=/tf --ip 0.0.0.0 --no-browser --allow-root --NotebookApp.password=$PASSWORD"]

