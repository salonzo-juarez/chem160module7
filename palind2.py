def palind2(s):
    alist=list()
    alist.reverse()
    revs="".join(alist)
    if revs==s:
        return True
    return False
print(palind2("ratsliveonnoevilstart"))
print(palind2("abcdedcba"))
