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
You are a QA engineer helping to generate a test case based on a prompt . Use this format, replacing text in brackets with the result. Do not include the brackets in the output:<br>
 [Title based on the prompt]<br>
 [Steps based on the prompt]<br>
 [Expected results based on the prompt]<br>
"""<br>
Login into app\n

The following suggestion will be delivered by openAI :

Title: Verify login into app 

Steps:
1. Navigate to the app login page
2. Enter valid username and password
3. Click the "Login" button

Expected Results:
1. User should be logged into the app successfully.

Once script finishes, the following message will display:

```Test Case created successfully in TestRail.```
