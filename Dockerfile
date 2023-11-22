FROM python
FROM node


COPY . /myTasks

WORKDIR /fronted
RUN npm install -g npm@latest
RUN npm run dev
WORKDIR /backend
RUN set -xe \
    && apt-get update -y \
    && apt-get install -y python3-pip
RUN pip install --no-cache-dir -r requirements.txt
RUN python main
