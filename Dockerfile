FROM python:3.10.9-slim-buster
RUN apt update && apt upgrade -y
RUN apt install git -y
WORKDIR /ANUSHKA
COPY requirements.txt /requirements.txt
CMD ["python", "bot.py"]
