#拉取一个基础镜像，基于python3.11
FROM python:3.11
# 维护者信息
MAINTAINER Xinyu
# 将你的项目文件放到docker容器中的/code/bdtools文件夹，这里code是在根目录的，与/root /opt等在一个目录
# 这里的路径，可以自定义设置，主要是为了方便对项目进行管理
ADD ./Server/ /code/Server/ 
# 设置容器时间，有的容器时区与我们的时区不同，可能会带来麻烦
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' >/etc/timezone 
# 设置语言为utf-8
ENV LANG C.UTF-8
# 设置工作目录，也就是下面执行 ENTRYPOINT 后面命令的路径
WORKDIR /code/Server
# 根据requirement.txt下载好依赖包
RUN /usr/local/bin/pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
# 根据requirement.txt下载好依赖包
# EXPOSE 指令是声明运行时容器提供服务端口，这只是一个声明，在运行时并不会因为这个声明应用就会开启这个端口的服务。
# 此处填写8000，是因为我们上面的app.py提供的web服务就需要使用8000端口
EXPOSE 8000 
ENTRYPOINT ["python3","app.py"]