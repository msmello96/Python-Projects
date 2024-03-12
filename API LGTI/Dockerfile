FROM python:3.10-slim
ENV PYTHONUNBUFFERED 1
RUN apt-get update -y
RUN apt-get install -y vim
WORKDIR /automacao/telefonia
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . ./
EXPOSE 8000
RUN python3 manage.py collectstatic
RUN python3 manage.py migrate
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]