# PaaS ProberS Web Application (Azure App Services Deployment)
This is the PaaS ProberS Django web application that was deployed on Azure App Services using [this link](https://test-web-app-azure.azurewebsites.net/).

## Build/Run Instructions
1. In the directory 'myenv/src', run the command 'python manage.py runserver' to run the web application on localhost.
2. Go to [localhost](http://127.0.0.1:8000/) to view the web application.
3. For access the database contents, use the [Django admin page](http://127.0.0.1:8000/admin/pages/).
4. To test this web application, use the provided script 'runner.py'. Type the command 'python runner.py -h' for information about using the script.

## Resources
* script 'runner.py' is in root directory
* sample input files (such as 'lorem_small.txt') are in root directory