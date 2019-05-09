def isStringPermutation(s1, s2):
    s1_dict = {}
    for i in s1:
        if i not in s1_dict:
            s1_dict[i] = 1
        else:
            s1_dict[i] = s1_dict[i] + 1
    s2_dict = {}
    for j in s2:
        if j not in s2_dict:
            s2_dict[j] = 1
        else:
            s2_dict[j] = s2_dict[j] + 1
    print(s1_dict, s2_dict)
    if s1_dict == s2_dict:
        permutation = True
    else:
        permutation = False
    return permutation


print(isStringPermutation("abababababa", "bbaaa"))
print(isStringPermutation("aaaabbb", "aaaabbb"))
print(isStringPermutation("bbbaa", "bbbaa"))
print(isStringPermutation(" abc", "c ab"))
