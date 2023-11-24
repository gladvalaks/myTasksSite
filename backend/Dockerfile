FROM ubuntu:latest
FROM python


COPY . /mytask
WORKDIR /mytask
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
CMD ["python", "main.py"]


