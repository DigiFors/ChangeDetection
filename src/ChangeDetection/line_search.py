from typing import List
from .detection import Detection


class LineSearchDetection(Detection):

    def __detect__(self, old: List[str], new: List[str]) -> List[str]:

        old_lines_set = set(old)

        new_lines_set = set(new)

        old_added = old_lines_set - new_lines_set
        old_removed = new_lines_set - old_lines_set

        res = []
        for line in old:
            if line in old_added:
                res.append('-' + line)
            elif line in old_removed:
                res.append('+' + line)

        for line in new:
            if line in old_added:
                res.append('-' + line)
            elif line in old_removed:
                res.append('+' + line)
            else:
                res.append('=' + line)
        return res
