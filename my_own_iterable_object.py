from datetime import timedelta, date


class DateRangeIterable:
    """
    자체 이터레이터 메서드를 가지고 있는 이터러블
    """

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._present_day = start_date

    def __iter__(self):
        return self

    def __next__(self):
        if self._present_day >= self.end_date:
            raise StopIteration
        day = self._present_day
        self._present_day += timedelta(days=1)
        return day


if __name__ == "__main__":
    for day in DateRangeIterable(date(2020, 1, 1), date(2020, 1, 5)):
        print(day)
    """
    2020-01-01
    2020-01-02
    2020-01-03
    2020-01-04
    """

    r = DateRangeIterable(date(2020, 1, 1), date(2020, 1, 5))
    for _ in range(6):
        print(next(r))
    """
    2020-01-01
    2020-01-02
    2020-01-03
    2020-01-04
    Traceback (most recent call last):
      File "/Users/marie/PycharmProjects/python-clean-code/my_own_iterable_object.py", line 37, in <module>
        print(next(r))
      File "/Users/marie/PycharmProjects/python-clean-code/my_own_iterable_object.py", line 19, in __next__
        raise StopIteration
    StopIteration
    """

