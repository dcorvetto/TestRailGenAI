# TestRailGenAI
Generate test cases in TestRail using openAI suggestions

EXAMPLE

In Terminal run the following

```
$ python3 integrateTestRailOpenAI.py
```

```Please enter test case description: Login into app```

The following prompt will be sent to openAI API:

"""<br>
You are a QA engineer helping to generate test scenarios based on a prompt. Based on each test scenario, help to generate at least 4 test cases. Use this format replacing text in brackets with the result. Do not include the brackets in the output:<br>
 Test case [number of test case]<br>
 [Title: title of test case based on the prompt]<br>
 [Steps: list of steps based on the prompt]<br>
 [Expected results: list of results based on the prompt]<br>
"""<br>
Login into app\n

The following suggestions will be delivered by openAI :

Test case 1
 Title: Check login functionality
 Steps:
 1. Enter valid username
 2. Enter valid password
 3. Click the login button
Expected results:
 1. User is logged in
 2. Home page of the application is displayed
 3. Successful login message is displayed
 4. User should be able to access the features of the application

Test case 2
 Title: Check login failure with invalid credentials
 Steps:
 1. Enter invalid username
 2. Enter invalid password
 3. Click the login button
Expected results:
 1. User is not logged in
 2. Login page should be displayed
 3. Error message is displayed
 4. User should not be able to access the features of the application
 
 ....

Once script finishes, the following messages will display:

```Total Tokens: 425
Test Case 1 created successfully in TestRail.
Test Case 2 created successfully in TestRail.```
