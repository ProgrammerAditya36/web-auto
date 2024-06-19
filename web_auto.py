#!/usr/bin/env python3
import os
path = os.getcwd()
while True:
    project = int(input("Enter the type of project:\n1.Frontend\n2.Django\n3.Fullstack MERN\n4.End\n"))
    if project == 1:
        projectname = input("Enter the project name: ")
        os.system("mkdir " + projectname)
        os.chdir(projectname)
        os.system("touch index.html")
        os.system("touch style.css")
        os.system("touch script.js")
        os.system("code .")
        break
    if project == 2:
        projectname = input("Enter the project name: ")
        appname = input("Enter the app name: ")
        
        ret = os.system("django-admin startproject " + projectname)
        if ret == 0:
            print("Project created successfully")
            os.chdir(projectname)
            os.system("python manage.py startapp " + appname)
            os.system("python manage.py runserver")
            break
        else:
            print("Error in creating project")
            c = int(input("Do you want to try again?\n1.Yes\n2.No\n"))
            if c == 2:
                break
    if project == 3:
        projectname = input("Enter the project name: ")
        os.system("create-vite "+projectname+" --template react-ts")
        os.chdir(projectname)
        os.system("npm install")
        os.system("npm run dev")
        break
    else:
        print("Invalid choice")
        continue
    if project == 4:
        break