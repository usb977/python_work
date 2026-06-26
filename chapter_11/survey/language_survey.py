from survey import AnonymousSurvey

question = "你的母语是什么？"
language_survey = AnonymousSurvey(question)

language_survey.show_question()
print("任何时候按下'q'即可退出程序。\n")
while True:
    response = input("请输入您的母语：")
    if response == 'q':
        break
    language_survey.store_response(response)

print("\n感谢每一位愿意参加本次问卷调查的人！")
language_survey.show_results()