# TestRailGenAI
Generate test cases in TestRail using openAI suggestions

- In Terminal run the following

$ python3 integrateTestRailOpenAI.py
Please enter test case description: Login into app

- The following prompt will be sent to openAI API:

"""
You are a QA engineer helping to generate a test case based on a prompt . Use this format, replacing text in brackets with the result. Do not include the brackets in the output:
 [Title based on the prompt]
 [Steps based on the prompt]
 [Expected results based on the prompt]
"""
Login into app\n

- The following suggestion will be delivered by openAI :

Title: Verify User Can Only See Assigned Location’s Resources 

Steps:
1. Log in to the application as a user who has selected a specific assigned location
2. Navigate to the Devices, Groups, Schedules, Controllers, and Scenes pages

Expected Results:
1. The user should only see resources that belong to their assigned location.

- Once script finishes, the following message will display:

Test Case created successfully in TestRail.
