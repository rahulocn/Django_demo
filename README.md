# Django_demo
Contains a model Project with API exposed and added the model to Admin
eg.
1. http://localhost:8000/api/prjapp/?format=json&name__contains=sav
returns JSON with project names containing string

2. http://localhost:8000/api/prjapp/?format=json&name=Amazon
returns JSON with project name matching it