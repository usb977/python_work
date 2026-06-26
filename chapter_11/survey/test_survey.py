import pytest
from survey import AnonymousSurvey

@pytest.fixture
def language_survey():
    """创建一个给所有测试例子用的对象"""
    question = "请输入您的母语："
    language_survey = AnonymousSurvey(question)
    return language_survey

def test_store_single_response(language_survey):   #需要传入对象作为形参
    """测试单个回答是否会被妥善存储"""
    language_survey.store_response('English')
    assert 'English' in language_survey.responses_

def test_store_three_responses(language_survey):
    responses = ['English','Spanish','Mandarin']
    for response in responses:
        language_survey.store_response(response)
    
    for response in responses:
        assert response in language_survey.responses_