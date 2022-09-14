import unittest
class AnonymousSurvey():
    """Collect anonymous answers to a survey question."""

    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question."""
        print(self.question)

    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)

    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print('- ' + response)

#This test is inneficient because we create one object per call to the method test_store_single_response. 
class TestAnonmyousSurvey(unittest.TestCase):
    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)
unittest.main() 

#To solve this we use the method set up
class TestAnonymousSurvey(unittest.TestCase):
    #Python runs the setUp() method before runningeach method starting with test_.
    def setUp(self): #In this method we create one object survey for all test methods. 
        """
        Create a survey and a set of responses for use in all test methods.
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']
        def test_store_single_response(self):
            """Test that a single response is stored properly."""
            self.my_survey.store_response(self.responses[0])
            self.assertIn(self.responses[0], self.my_survey.responses)

        def test_store_three_responses(self):
            """Test that three individual responses are stored properly."""
            for response in self.responses:
                self.my_survey.store_response(response)
            for response in self.responses:
                self.assertIn(response, self.my_survey.responses)
unittest.main() 