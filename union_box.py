
from union_interface import UnionInterface


class UnionBox(UnionInterface):
    """
    Union Box

    From a graph of boxes, get the union of boxes

    Example:
    4 |                   ______
    3 |     ____         |    __|_______________
    2 |   _|__  |    ____|   |  |               |
    1 |  | |  | |   |    |   |  |               |
    0 |__|_|__|_|___|____|___|__|_______________|________
         2 4  7 9   13   18  22 25              40

    union = [
        # Illustrates the first set of boxes:
        (2, 0), (2, 2), (4, 2), (4, 3), (9, 3), (9, 0),
        # Illustrates the second set of boxes:
        (13, 0), (13, 2), (18, 2), (18, 4), (25, 4), (25, 3), (40, 3), (40, 0)
    ]

    (Visual representation):

     4 |                    ______
     3 |      ____         |      |_______________
     2 |    _|    |    ____|                      |
     1 |   |      |   |                           |
     0 |___|______|___|___________________________|________
           2 4  7 9   13   18  22 25              40

    """

    def merge(self, l, r):
        lcur = 0
        rcur = 0
        out = []
        if len(l) == 0 or len(r) == 0:
            if len(l) == 0:
                if len(r) == 0:
                    return []
                return (r)
            if len(r) == 0:
                return (l)
        if(l[0][0] < r[0][0]):
            cur = 0
            out.append(l[0])
            lcur += 1
        elif(l[0][0]>r[0][0]):
            out.append(r[0]) 
            rcur += 1
            cur = 1
        else:
            out.append(l[0])
            cur = 0
            lcur+= 1
            rcur+= 1
        while lcur<len(l) and rcur<len(r):
            if l[lcur][0] == r[rcur][0]:
                if l[lcur][1] >= r[rcur][1]:
                    out.append(l[lcur])
                else:
                    out.append(r[rcur])
                lcur+= 1
                rcur+= 1
            elif l[lcur][0]<r[rcur][0] and cur == 0:
                if l[lcur][1]<r[rcur][1]:
                    out.append((l[lcur][0], r[rcur][1]))
                    cur = 1
                else:
                    out.append(l[lcur])
                    lcur += 1
            elif r[rcur][0]<l[lcur][0] and cur == 1:
                if r[rcur][1]<l[lcur][1]:
                    out.append((r[rcur][0], l[lcur][1]))
                    cur = 0
                else:
                    out.append(r[rcur])
                    rcur += 1
            elif r[rcur][0]<l[lcur][0] and cur == 0:
                if r[rcur][1]<l[lcur][1]:
                    rcur+= 1
                else:
                    out.append((r[rcur][0], l[lcur][1]))
                    cur = 1
            else:
                if l[lcur][1]<r[rcur][1]:
                    lcur+= 1
                else:
                    out.append((l[lcur][0], r[rcur][1]))
                    cur = 0
        if lcur == len(l):
            if rcur == len(r):
                pass
            else:
                while rcur < len(r):
                    out.append(r[rcur])
                    rcur+= 1
        else:
            while lcur < len(l):
                out.append(l[lcur])
                lcur+= 1
        x = 1
    y = 1
    X = 0
    Y = 0
    c = 0
    ToDel = []
    while(c<len(out)):
        if out[c][0] == X:
            x += 1
        else:
            x = 1
        if x >= 3:
            ToDel.insert(0,c-1)
        if out[c][1] == Y:
            y += 1
        else:
            y = 1
        if y >= 3:
            if len(ToDel) >0 and ToDel[0] == c-1:
                pass
            else:
                ToDel.insert(0,c-1)
        X = out[c][0]
        Y = out[c][1]
        c += 1
    c = 0
    while(c<len(ToDel)):
        del out[ToDel[c]]
        c += 1
    return out
        """
        Merge the two "boxes" together.
           ____           ____
         _|__  |        _|    |
        | |  | |  ==>  |      |
        |_|__|_|       |      |

        Example:
        input:
            l: [ (2,0), (2,2), (7,2), (7,0) ]
            r: [ (4,0), (4,3), (9,3), (9,0) ]
        return:
            [ (2,0), (2,2), (4,2), (4,3), (9,3), (9,0) ]

        :param l: Array of coordinates representing one box.
        :param r: Array of coordinates representing another box.
        :return: The merged coordinates to present.
        """
        # TODO implement me.
        return []

    def union(self, box_list):
        """
        Performs the union of a list of boxes (in the form of x, y coordinate tuples)

        e.g. box_list = [ [(2,2), (2, 2), (7, 2), (7, 0)], [(4,0), (4,3), (9,3), (9,0)] ]
        :param box_list: List of boxes represented as coordinates.
        :return: The union of all the boxes.  (As presented in the example above)
        """
        if not box_list:
            return []

        if len(box_list) == 1:
            return box_list[0]

        if len(box_list) == 2:
            left_box = box_list[0]
            right_box = box_list[1]
            merged = self.merge(left_box, right_box)
            return merged

        # Else, time to do me a recursion
        left_list = self.union(box_list[:int(len(box_list) / 2)])
        right_list = self.union(box_list[int(len(box_list) / 2):])
        merged = self.merge(left_list, right_list)
        return merged
