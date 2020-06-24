# Dockerfile - this is a comment. Delete me if you want.
FROM python:3.6.1
RUN pip install --upgrade pip
COPY . /application
WORKDIR /application
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
ENTRYPOINT ["python"]
CMD ["main.py"]