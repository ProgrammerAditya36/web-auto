#!/usr/bin/env python3
import os
import sys
path = os.getcwd()
while True:
    args = sys.argv[1:]
    project = args[0]
    if project == "1" or project == "fe":
        projectname  = args[1] if len(args) > 1 else "mywebapp"
        os.system("mkdir " + projectname)
        os.chdir(projectname)
        os.system("touch index.html")
        with open("index.html", "w") as f:
            f.write("<!DOCTYPE html>\n<html>\n<head>\n<title></title>\n<link rel='stylesheet' href='style.css'>\n</head>\n<body>\n<script src='script.js'></script>\n</body>\n</html>")
        os.system("touch style.css")
        os.system("touch script.js")
        os.system("code .")
        break
    if project == "2" or project == "django":
        projectname = args[1] if len(args) > 1 else "mydjangoapp"
        appname = args[2] if len(args) > 2 else None  
        ret = os.system("django-admin startproject " + projectname)
        if ret == 0:
            print("Project created successfully")
            os.chdir(projectname)
            if(appname is not None):                
                os.system("python manage.py startapp " + appname)
            os.system("code .")        
            os.system("python manage.py runserver")
            break
        else:
            print("Error in creating project")
            c = int(input("Do you want to try again?\n1.Yes\n2.No\n"))
            if c == 2:
                break
    if project == "3" or project == "react":
        projectname = args[1] if len(args) > 1 else "my-react-app"
        os.system("create-vite "+projectname+" --template react-ts")
        os.chdir(projectname)
        os.system("npm install")
        os.system("code .")
        os.system("npm run dev")
        break
    if project == "4" or project == "node":
        projectname = args[1] if len(args) > 1 else "my-node-app"
        os.system("mkdir " + projectname)
        os.chdir(projectname)
        os.system("npm init -y")
        os.system("npm install express")
        os.system("touch index.js")
        with open("index.js", "w") as f:
            f.write("const express = require('express')\nconst app = express()\napp.get('/', (req, res) => {\nres.send('Hello World!')\n})\napp.listen(3000, () => {\nconsole.log('Server is running on http://localhost:3000')\n})")
        os.system("code .")        
        os.system("npx nodemon index.js")
        break
    if project == 5:
        break
    else:
        print("Invalid choice")
        continue