FROM python:2.7
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
ADD __init__.py /opt/__init__.py
ADD config.py /opt/config.py
ADD run.py /opt/run.py
ADD app /opt/app
WORKDIR /opt
EXPOSE 5000
CMD ["python", "run.py"]
