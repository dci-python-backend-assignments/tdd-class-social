## Set Project Key as environmental variable in Pycharm's run configurations menu.
** **
### please do the following...

  1. Open the Run Configuration selector in the top-right corner *Edit Configurations...*
  2. find Environmental variable and click on the icon on left side of the line to edit
  3. click on Plus sign to add new variable, provide a NAME(use this name "DETA_PROJECT_KEY") and VALUE_
** **
 IMPORTANT 
 - You can access your project key with os.environ 
      ```PY
   import os 
   token = os.environ.get("DETA_PROJECT_KEY")
 - !!! All devops are required to Use the SAME environmental variable!!!

 - Please reach the Product Owner or the Developer of this Issue to get the Project Key