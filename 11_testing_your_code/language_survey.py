from survey import AnonymousSurvey

# Define a question, and make a survey.
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question=question)

# Show the question, and store responses to the question.
my_survey.show_question()
print("Enter 'q' anytime to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(new_response=response)

# Show the survey results.
print("\nThank you all for participating in this survey!\n")
my_survey.show_results()