import re

EMAIL_FORMAT = re.compile(r"[^@]+@[^@]+[^@]+")


def is_valid_email(potentially_valid_email: str):
    return re.match(EMAIL_FORMAT, potentially_valid_email) is not None


class User:
    def __init__(self, username):
        self.username = username
        self._email = None

    # 무언가에 응답하기 위한 데코레이터: @property
    @property
    def email(self):
        return self._email

    # 무언가를 하기 위한 커맨드: @<property_name>.setter
    # <user>.email = <new_email>이 호출 될때의 아래 함수 실행
    @email.setter
    def email(self, new_email):
        if not is_valid_email(new_email):
            raise ValueError(f"유효한 이메일이 아님으로 {new_email} 값을 사용할 수 없음")
        self._email = new_email


if __name__ == "__main__":
    u1 = User("jsmith ")
    u1.email = "jsmith@gmail.com"
    print(u1.email)





