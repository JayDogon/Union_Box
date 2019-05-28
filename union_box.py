def merge(l, r):
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
                return out
            else:
                while rcur < len(r):
                    out.append(r[rcur])
                    rcur+= 1
                return out
        while lcur < len(l):
            out.append(l[lcur])
            lcur+= 1
        return out


#L = [ (2,0), (2,2), (4,2), (4,0) ]
#R = [ (4,0), (4,4), (8,4), (8,0) ]

#RR = [ (8,0), (8,2), (18,2), (18,0) ]
#LL = merge(L, R)

R = [ (2,0), (2,2), (7,2), (7,0) ]
L = [ (4,0), (4,4), (5,4), (5,0) ]

input(merge(L,R))
