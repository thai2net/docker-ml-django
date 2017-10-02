# docker-ml-django

## Prerequisite
1. Install Docker
- Docker for Mac https://docs.docker.com/docker-for-mac/install/
- Docker for Windows 10 https://docs.docker.com/docker-for-windows/install/
2. Download or clone this repository

## Start docker container
1. Open terminal or cmd on Windows 
2. Go to "docker-ml-django" folder
3. Execute the command below
```bash
docker-compose up --build
```
4. Wait until you see something like this
```bash
mlapi    | Performing system checks...
mlapi    | 
mlapi    | System check identified no issues (0 silenced).
mlapi    | 
mlapi    | You have 13 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
mlapi    | Run 'python manage.py migrate' to apply them.
mlapi    | 
mlapi    | October 02, 2017 - 18:57:51
mlapi    | Django version 1.11.5, using settings 'sidtechtalent.settings'
mlapi    | Starting development server at http://0.0.0.0:8000/
```
Now we're good to go

## Access exmaple API
Open browser and browse to
```
http://localhost:8000/api/hello
```

## ML implementation
Implement your ML code at
```txt
sidtechtalent/api/views.py
```

Then update path at 
```txt
sidtechtalent/sidtechtalent/urls.py
```
