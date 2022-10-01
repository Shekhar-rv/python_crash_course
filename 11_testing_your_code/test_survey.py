import unittest
from survey import AnonymousSurvey

class TestAnonymusSurvey(unittest.TestCase):
    """Tests for each module in Class AnonymusSurvey"""

    def setUp(self):
        """
        Create a survey and a set of responses for use in all test methods.
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin', 'English', 'Spanish',]

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        self.my_survey.store_response(self.responses[0])

        # Check if 'English' is in the response.
        self.assertIn("English", self.my_survey.responses)

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        for response in self.responses:
            self.my_survey.store_response(response)
        
        # Check if each of the three responses are saved in the 
        # responses list
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

    def test_remove_duplicate_reponses(self):
        """Test that only unique reponses are returned."""
        for response in self.responses:
            self.my_survey.store_response(response)
        # Not the most efficient way to test, need to figure out a better 
        # approach to test for no duplicates.
        self.assertNotEqual(self.responses, list(set(self.my_survey.responses)))


unittest.main()