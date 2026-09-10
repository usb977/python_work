from python_repos import get_url_state

def test_url_state():
    """能够正确输出url的状态吗"""
    url_state = get_url_state("https://api.github.com/search/repositories?q=language:python+sort:stars+stars:>10000" )
    assert url_state == True


