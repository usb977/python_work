class AnonymousSurvey:
    
    def __init__(self,question):
        self.question_ = question
        self.responses_ = []

    def show_question(self):
        print(self.question_)
    
    def store_response(self,new_response):
        self.responses_.append(new_response)
    
    def show_results(self):
        print("调查结果为：")
        for response in self.responses_:
            print(f"- {response}")