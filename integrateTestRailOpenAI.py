import requests
import json
import openai
import config
import time

# TestRail Authentication
URL = config.testRail_URL
USERNAME =  config.testRail_username
PASSWORD = config.testRail_password
project_id = config.testRail_project_id
suite_id = config.testRail_suite_id
section_id = config.testRail_section_id

# Inputs
openai_prompt_input = input("Please enter test case description: ")

# Generate OpenAI test case
openai_api_key = config.openai_api_key
openai_prompt = """
You are a QA engineer helping to generate test scenarios based on a prompt. Based on each test scenario, help to generate at least 4 test cases. Use this format replacing text in brackets with the result. Do not include the brackets in the output:
Test case [number of test case]
 [Title: title of test case based on the prompt]
 [Steps: list of steps based on the prompt]
 [Expected results: list of results based on the prompt]
""" + openai_prompt_input + r"\n"

print(openai_prompt) 

openai.api_key = openai_api_key

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=openai_prompt,
  temperature=0.6,
  max_tokens=450,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

time.sleep(5)


if 'choices' in response:
        if len(response['choices']) > 0: 
            answer = response['choices'][0]['text']
            tokens = response['usage']['total_tokens']
        else:
            answer = 'Opps sorry, you beat the AI this time'
else:
    answer = 'Opps sorry, you beat the AI this time'


print(answer)
print("Total Tokens: " + str(tokens))


test_cases = answer.split("Test case")

i = 0
for tc in test_cases:
    if i > 0 :
        tc_aux = tc.replace("Test case", "")
        test_case_text_aux1 = tc_aux.replace("Title:", "|")
        test_case_text_aux2 = test_case_text_aux1.replace("Steps:", "|")
        test_case_text_aux3 = test_case_text_aux2.replace("Expected results:", "|")

        test_case_text = test_case_text_aux3.split("|")
        if len(test_case_text) > 3:
            title = test_case_text[1].replace("|","")
            steps = test_case_text[2].replace("|","")
            test_case_title = title
            test_case_steps = steps
            test_case_expected_results = test_case_text[3]

            # Create test case in TestRail
            testrail_url = f"{URL}/index.php?/api/v2/add_case/{section_id}"
            testrail_headers = {
                "Content-Type": "application/json"
            }
            testrail_payload = {
                "title": test_case_title,
                "custom_steps": test_case_steps,
                "custom_expected": test_case_expected_results,
                "suite_id": suite_id,
                "section_id": section_id
            }
            response = requests.post(testrail_url, auth=(USERNAME, PASSWORD), headers=testrail_headers, json=testrail_payload)

            if response.status_code == 200:
                print("Test Case " +str(i)+ " created successfully in TestRail.")
            else:
                print("Error creating test case " +str(i)+ " in TestRail:", response.content)
        
    i += 1