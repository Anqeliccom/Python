def reverseDict(firstDict):
    revDict = {}

    for key, value in firstDict.items():
        if value not in revDict:
            revDict[value] = [key]
        else:
            revDict[value].append(key)

    for key, value in revDict.items():
        revDict[key] = value[0] if len(value) == 1 else tuple(value)

    return revDict

firstDict = {"Ivanov": 97832, "Petrov": 55521, "Kuznecov": 97832}
revDict = reverseDict(firstDict)

print(revDict)





