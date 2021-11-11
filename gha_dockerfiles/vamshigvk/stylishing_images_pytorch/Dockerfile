FROM public.ecr.aws/lambda/python:3.7
RUN yum update -y
#RUN apt-get install -y libncurses5-dev libncursesw5-dev libtinfo5
COPY . ${LAMBDA_TASK_ROOT}/
RUN pip install --upgrade pip

RUN python -m pip install --target ${LAMBDA_TASK_ROOT}/ torch==1.7.1 -f https://download.pytorch.org/whl/torch_stable.html
RUN pip install --target ${LAMBDA_TASK_ROOT}/  torchvision===0.8.2 -f  https://download.pytorch.org/whl/torch_stable.html
RUN pip install --target ${LAMBDA_TASK_ROOT}/  opencv-python==4.1.0.25
RUN pip install --target ${LAMBDA_TASK_ROOT}/  numpy==1.16.3
RUN pip install --target ${LAMBDA_TASK_ROOT}/  matplotlib==3.0.3
#CMD python stylize.py
CMD [ "lambda_function.lambda_handler" ]
