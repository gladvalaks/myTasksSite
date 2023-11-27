
FROM python


COPY . /backend
WORKDIR /backend
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
CMD ["python", "main.py"]
EXPOSE 3001


