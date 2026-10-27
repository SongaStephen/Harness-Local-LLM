from solution import BoundedQueue


def test_peek_returns_front_without_removing():
    q = BoundedQueue(3)
    q.enqueue(1)
    q.enqueue(2)
    assert q.peek() == 1
    assert q.dequeue() == 1  # peek must not have removed it


def test_is_full_true_at_capacity():
    q = BoundedQueue(2)
    q.enqueue(1)
    q.enqueue(2)
    assert q.is_full() is True


def test_is_full_false_below_capacity():
    q = BoundedQueue(2)
    q.enqueue(1)
    assert q.is_full() is False
