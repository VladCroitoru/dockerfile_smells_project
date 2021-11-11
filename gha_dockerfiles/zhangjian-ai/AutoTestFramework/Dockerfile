FROM python:3.8.5-slim
COPY ./requirements.txt /depends/rerequirements.txt
COPY ./nodeServer.py /depends/nodeServer.py
# DEBIAN_FRONTEND这个环境变量，告知操作系统应该从哪儿获得用户输入。
# 如果设置为”noninteractive”，你就可以直接运行命令，而无需向用户请求输入（所有操作都是非交互式的）。
# 这在运行apt-get命令的时候格外有用，因为它会不停的提示用户进行到了哪步并且需要不断确认。
# 非交互模式会选择默认的选项并以最快的速度完成构建。
RUN BEBIAN_FRONTEND=noninteractive apt-get update && \
    apt-get upgrade -yq && \
    apt-get install --no-install-recommends -yq gcc python-dev && \
    pip install -i https://pypi.doubanio.com/simple -r /depends/rerequirements.txt
    # 修改allure报告用例标题样式，修改allure报告中用例标题后面的参数为空
    # sed -i 's/Parameter(name=name, value=represent(value)) for name, value in params.items()//' /usr/local/lib/python3.8/site-packages/allure_pytest/listener.py
WORKDIR /pytest_workdir
# 保持主进程不退出
CMD ["sh", "-c", "while true; do sleep 1; done"]