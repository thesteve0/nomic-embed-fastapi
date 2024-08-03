FROM pytorch/pytorch:2.3.1-cuda11.8-cudnn8-runtime

LABEL authors="spousty"

# Set the current working directory to /code.
# This is where we'll put the requirements.txt file and the app directory.
WORKDIR /app

# Copy the file with the requirements to the /app directory.
# Copy any python files into the /app directory
COPY ./requirements.txt *.py ./

# Install the package dependencies in the requirements file.
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Set the command to run the uvicorn server.
# CMD takes a list of strings, each of these strings is what you would type in the command line separated by spaces.
CMD ["uvicorn", "main:app", "--host", "::", "--port", "80"]
#CMD ["fastapi", "run", "main.py", "--port", "8234"]