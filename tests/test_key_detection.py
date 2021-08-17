import pytest
from src.ChangeDetection.key_detection import KeyDetection


@pytest.mark.parametrize(
    "old, new, result, works",
    [
        ("abcd", "abcdz", ['=a', '=b', '=c', '=d', '+z'], True),
        ("abcd", "abzcd", ['=a', '=b', '+z', '=c', '=d'], True),
        ("abcd", "dbca", ['=a', '=b', '=c', '=d'], False),

    ]
)
def test_added_lines(old, new, result, works:bool):
    detection = KeyDetection()
    changes = detection.detect(old, new)
    if works:
        assert changes == result
    else:
        assert changes != result
