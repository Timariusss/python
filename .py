import time


def measure_time(func, *args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    return result, end - start


def test_simple():
    def slow():
        time.sleep(0.1)
        return "ok"

    result, t = measure_time(slow)

    assert result == "ok"
    assert t >= 0.1
if __name__ == "__main__":
    import pytest
    pytest.main()