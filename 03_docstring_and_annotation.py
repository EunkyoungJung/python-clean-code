def data_from_response(response: dict) -> dict:
    """response에 문제가 없다면 response의 payload를 반환생

    - response 사전의 예제::
    {
        "status": 200, # <int>
        "timestamp": "....", # 현재 시간의 ISO 포맷 문자열
        "payload": { ... } # 반환하려는 사전 데이터
    }

    - 반환 사전 값의 예제::
    {"data": { .. } }

    - 발생 가능한 예외:
    - HTTP status가 200이 아닌 경우 ValueError 발
    """
    if response['status'] != 200:
        raise ValueError
    return {"data": response["payload"]}


# print(data_from_response.__annotations__)
# """
# {'response': <class 'dict'>, 'return': <class 'dict'>}
# """
# print(data_from_response.__doc__)
# """
# None
# """

# data_from_response(1)
# """
# Traceback (most recent call last):
#   File "/Users/marie/PycharmProjects/python-clean-code/03_docstring_and_annotation.py", line 17, in <module>
#     data_from_response(1)
#   File "/Users/marie/PycharmProjects/python-clean-code/03_docstring_and_annotation.py", line 2, in data_from_response
#     if response['status'] != 200:
# TypeError: 'int' object is not subscriptable
#
# Process finished with exit code 1
# """
