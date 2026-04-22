# Use Python image
FROM python:3.12-slim

#Set working dir
WORKDIR /alpha

#Copy files 
COPY . .

#Install dependencies 

RUN pip install --no--cache-dir -r requirements.txt 

#Collect static files
RUN python manage.py migrate 

#Expose port 
EXPOSE 80000

# start server 
CMD ["gunicon", "alpha.wsgi:application", "--bind", "0.0.0.0:80000"]

