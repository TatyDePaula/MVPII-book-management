FROM python:latest
WORKDIR /flaskProject1
COPY requirements.txt /flaskProject1/
COPY db.py .
RUN pip install --no-cache-dir -r /flaskProject1/requirements.txt
COPY app.py /flaskProject1/
COPY templates/index.html /flaskProject1/templates/
COPY templates/templatecriarlivro.html /flaskProject1/templates/
COPY templates/templateeditarlivro.html /flaskProject1/templates/
COPY db.db .
COPY templates/visualizarlivro.html /flaskProject1/templates/
EXPOSE 5000
CMD ["python", "/flaskProject1/app.py"]

