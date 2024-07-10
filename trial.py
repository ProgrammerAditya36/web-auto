import os
page_name='react_website'
home_link = os.getenv("HOMEPAGE")
homepage = f"{home_link}{page_name}"
username = os.getenv("USERNAME")
print(homepage, username)