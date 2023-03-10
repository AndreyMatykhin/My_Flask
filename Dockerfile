from python:3.10.6

RUN apt-get update
RUN apt-get upgrade -y
RUN pip3 install --upgrade pip

WORKDIR /mainapp
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY wsgi.py wsgi.py
COPY My_Blog ./My_Blog
EXPOSE 5000
CMD ["python", "wsgi.py"]