from typing import List
from .detection import Detection


class RelationshipDetection(Detection):

    def __detect__(self, old: str, new: str) -> List[str]:

        res = []

        for old_id in range(len(old)):
            try:
                index = new.index(old[old_id])
            except ValueError:
                index = -1

            if index < 0:
                res.append('-' + old[old_id])
            else:
                if index >= 1:
                    for new_id in range(index):
                        res.append('+' + new[new_id])
                res.append('=' + old[old_id])
                new = new[index+1:]
        for new_id in range(len(new)):
            res.append('+' + new[new_id])
        return res
