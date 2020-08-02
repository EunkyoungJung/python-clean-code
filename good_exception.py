"""
올바른 수준의 추상황 단계에서 예외 처리
- 예외는 오직 한 가지 일을 하는 함수의 한 부분이어야 한다.
- 함수가 처리하는 (또는 발생시키는) 예외는 캡슐화된 로직과 일치해야 한다.
- 다음은 서로 다른 수준의 추상화를 혼합하는 예제이다.
- 애플리케이션에서 디코딩한 데이터를 외부 컴포넌트에 전달하는 객체를 상상해보자.
- deliver_event 메서드를 중점적으로 살펴보자.
"""


class DataTransport:
    """
    다른 레벨에서 예외를 처리하는 객체의 예
    """

    retry_threshold: int = 5
    retry_n_times: int = 3

    def __init__(self, connector):
        self._connector = connector
        self.connection = None

    def deliver_event(self, event):
        try:
            self.connect()
            data = event.decode()
            self.send(data)
        except ConnectionError as e:
            logger.info(f"연결 실패: {e}")
            raise
        except ValueError as e:
            logger.error(f"{event} 잘못된 데이터 포함: {e}")
            raise

    def connnect(self):
        for _ in range(self.retry_n_times):
            try:
                self.connection = self._connector.connect()
            except ConnectionError as e:
                logger.info(f"{e}: 새로운 연결 시도 {self.retry_threshold}")
                time.sleep(self.retry_threshold)
            else:
                return self.connection
        raise ConnectionError(f"{self.retry_n_times}번째 재시도 연결 실패")

    def send(self, data):
        return self.connection.send(data)


