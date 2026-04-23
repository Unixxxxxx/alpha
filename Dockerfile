# Use Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /alpha

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8000

# Start server
CMD ["gunicorn", "alpha.wsgi:application", "--bind", "0.0.0.0:8000"]