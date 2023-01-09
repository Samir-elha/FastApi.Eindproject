FROM python:3.8
ADD requirements.txt /requirements.txt
ADD main.py /main.py
ADD okteto-stack.yaml /okteto-stack.yaml
RUN pip install -r requirements.txt
EXPOSE 8080
COPY ./todooo todooo
CMD ["python3", "main.py"]

#FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
#COPY requirements.txt /
#RUN pip install -r /requirements.txt
#COPY ./todooo /todooo/app