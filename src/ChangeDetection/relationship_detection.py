from typing import List, Optional
from .detection import Detection
import numpy as np
import random


def __evaluate__(old: str, new: str, weights: Optional[List[float]] = None) -> List[str]:
    if weights is None:
        weights = [0] * len(old)
    res = []

    old_id = 0
    while old_id < len(old):
        start = old_id
        end = old_id + 1 + abs(round(weights[old_id]))
        token = old[start:end]
        index = new.find(token)

        if index < 0:
            res.append('-' + token)
        else:
            if index >= 1:
                res.append('+' + new[:index])
            res.append('=' + token)
            new = new[index + len(token):]
        old_id = end
    if new:
        res.append('+' + new)
    return res


def get_components(changes):
    neutrals = []
    rest = []
    for change in changes:
        if change[0] == '=':
            neutrals.append(change)
        else:
            rest.append(change)
    return neutrals, rest


def get_max_len(changes):
    res = []
    if not changes:
        return 0
    for change in changes:
        res.append(len(change))
    return max(res)-1


def rank(old, new):
    new_neutrals, new_rest = get_components(new)
    old_neutrals, old_rest = get_components(old)
    diff_neutral = get_max_len(new_neutrals) - get_max_len(old_neutrals)
    diff_rest = get_max_len(new_rest) - get_max_len(old_rest)
    diff_change = len(new) - len(old)
    return diff_change - 2*diff_neutral + diff_rest


def simplify_changes(changes):
    res = [changes[0]]
    for i in range(1, len(changes)):
        change = changes[i]
        key = change[0]
        value = change[1:]
        if key == res[-1][0]:
            res[-1] = res[-1] + value
        else:
            res.append(change)
    return res


class RelationshipDetection(Detection):
    def __detect__(self, old: str, new: str) -> List[str]:
        size = len(old)
        x0 = np.zeros(size)
        dx = np.ones(size)

        changes = __evaluate__(old, new, list(x0))
        delta_changes = len(changes)
        best = changes

        for iterator in range(int(size/2)):

            counter = 0
            while abs(delta_changes) > 0:
                gradient = np.zeros(size)
                for i in range(size):
                    x = x0.copy()
                    x[i] += dx[i]
                    dchange = __evaluate__(old, new, list(x))
                    diff = rank(changes, dchange)
                    gradient[i] = diff/dx[i]
                x = x0.copy() - gradient
                new_changes = __evaluate__(old, new, list(x))

                delta_changes = rank(changes, new_changes)
                if counter > 10:
                    break
                elif list(gradient) == list(np.zeros(size)):
                    break
                changes = new_changes
                x0 = x
                counter = counter + 1

            if rank(best, changes) < 0:
                best = changes
            x0 = np.random.rand(size)
            changes = __evaluate__(old, new, list(x0))
            delta_changes = len(changes)

        return simplify_changes(best)






