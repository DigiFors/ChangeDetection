import pytest
from src.ChangeDetection.line_search import LineSearchDetection


@pytest.mark.parametrize(
    "old, new, result, works",
    [
        ("a b c d", "a b c d z", ['=a', '=b', '=c', '=d', '+z'], True),
        ("a b c d", "a b z c d", ['=a', '=b', '+z', '=c', '=d'], True),
        ("a b c d", "d b c a", ['=a', '=b', '=c', '=d'], False),

    ]
)
def test_added_lines(old, new, result, works:bool):
    detection = LineSearchDetection()
    changes = detection.detect(old, new)
    if works:
        assert changes == result
    else:
        assert changes != result
