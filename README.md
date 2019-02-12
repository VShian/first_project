# first_project
The app takes a scanned image of passport and displays the Name and Address of the person given in the passport.

## Requirements:
- django 2.0 or higher
- python 3.6 or higher
- pytesseract

## Running
- In the command prompt type **`python manage.py runserver`** to run the app.  
- Go to http://127.0.0.1:8000/image/ in your web browser.  
- Give a name in the description of the image **Mandatory**.  
- choose an image to upload.  
- click on **Upload button** to submit.  
- You are redirected to a new page in which the details of the person are shown. The details are Surname, Name, Address.
