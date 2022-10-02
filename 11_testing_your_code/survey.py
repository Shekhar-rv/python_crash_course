class AnonymousSurvey():
    """Collect anonymous answers to a survey question."""

    def __init__(self, question:str):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question."""
        print(self.question)

    def store_response(self, new_response:str):
        """Store a single response to the survey."""
        if new_response not in self.responses:
            self.responses.append(new_response)

    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        # We will remove duplicate responses
        # self.responses = list(set(self.responses))
        for response in self.responses:
            print('- ' + response)

if __name__ == '__main__':
    test = AnonymousSurvey("How is it in North America?")
    test.show_question()
    test.store_response("Couldn't be any better!")
    test.show_results()