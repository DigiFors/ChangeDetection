import pytest
from src.ChangeDetection import RelationshipDetection
from src.ChangeDetection.relationship_detection import __evaluate__, get_components


@pytest.mark.parametrize(
    "old, new, result, works",
    [
        ("abcd", "abcdz", ['=a', '=b', '=c', '=d', '+z'], True),
        ("abcd", "abzcd", ['=a', '=b', '+z', '=c', '=d'], True),
        ("abcd", "dbca", ['=a', '=b', '=c', '=d'], False),
        ("abcd", "dbca", ['+dbc', '=a', '-b', '-c', '-d'], True),
        ("aabb", "aazbb", ['=a', '=a', '+z', '=b', '=b'], True),
        ("affe", "apfel affe", ['+apfel', '=affe'], False),
    ]
)
def test_evaluate(old, new, result, works: bool):
    changes = __evaluate__(old, new)
    if works:
        assert changes == result
    else:
        assert changes != result


@pytest.mark.parametrize(
    "changes, result, works",
    [
        (['=abcd', '+z'], ['=abcd'], True),
        (['=ab', '=c', '=d', '+z'], ['=ab', '=c', '=d'], True),
    ]
)
def test_get_neutrals(changes, result, works: bool):
    neutrals,_ = get_components(changes)
    if works:
        assert neutrals == result
    else:
        assert neutrals != result


@pytest.mark.parametrize(
    "old, new, weights, result, works",
    [
        ("abcd", "abcdz", [3, 2, 1, 0], ['=abcd', '+z'], True),
        ("abcd", "abcdz", [1, 0, 0, 0], ['=ab', '=c', '=d', '+z'], True),
    ]
)
def test_evaluate_numbers(old, new, weights, result, works: bool):
    changes = __evaluate__(old, new, weights)
    if works:
        assert changes == result
    else:
        assert changes != result


@pytest.mark.parametrize(
    "old, new, result, works",
    [
        ("abcd", "abcdz", ['=abcd', '+z'], True),
        ("abcd", "abzcd", ['=ab', '+z', '=cd'], True),
        ("abcd", "dbca", ['+dbc', '=a', '-bcd'], True),
        ("abcd", "dbca", ['+dbc', '=a', '-bcd'], True),
        ("aabb", "aazbb", ['=aa', '+z', '=bb'], True),
        ("affe", "apfel affe", ['+apfel ', '=affe'], True),

    ]
)
def test_detection(old, new, result, works: bool):
    detection = RelationshipDetection()
    changes = detection.detect(old, new)
    if works:
        assert len(changes) <= len(result)
    else:
        assert changes != result
    detection.print()


@pytest.mark.parametrize(
    "old, new, result, works",
    [
        ("aabb", "aazbb", ['=aa', '+z', '=bb'], True),

    ]
)
def test_detection_special(old, new, result, works: bool):
    detection = RelationshipDetection()
    changes = detection.detect(old, new)
    if works:
        assert changes == result
    else:
        assert changes != result
    detection.print()
