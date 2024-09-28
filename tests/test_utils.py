from ..utils import get_name_from_url

def test_get_name_from_url():
    test_url = "https://picture-cdn04.zhcxkj.com/Aliexpress-Z04448-TOY-测试1_5544739143656657812/1/ProductImages/17548418/2023/09/18/8456e05958a14dc8bc1dddd02bc0d09e/99a02ff6-8575-446b-bb6d-de71d0ba4975.jpg?x-oss-process=image/resize,m_pad,w_800,h_800,limit_0,color_ffffff"
    
    assert get_name_from_url(test_url) == ("99a02ff6-8575-446b-bb6d-de71d0ba4975", ".jpg")


def test_get_name_from_url_without_qs():
    test_url = "https://ae01.alicdn.com/kf/S8be4ef631fa74f4c803406d130825a60V.jpg"

    assert get_name_from_url(test_url) == ("S8be4ef631fa74f4c803406d130825a60V", ".jpg")