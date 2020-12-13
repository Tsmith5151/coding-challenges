def rotateString(A: str, B: str) -> bool:
    if A == "" and B == "":
        return True

    a = [i for i in A]
    b = [i for i in B]

    for i in range(len(a)):
        tmp = a[0]
        a.pop(0)
        a.append(tmp)
        if a == b:
            return True
    return False