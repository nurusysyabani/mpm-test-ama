
def break_string(s, dictionary):
    n = len(s)
    list_result = []

    for i in range(n):
        for segment in range(i + 1, n + 1):
            for word in dictionary:
                if s[i : segment] == word:
                    list_result.append(s[i : segment])

    string_result = ', '.join(list_result)
    return string_result

print('program:', break_string('program', ['pro', 'gram', 'merit', 'program', 'it', 'programmer']))
print('programit:', break_string('programit', ['pro', 'gram', 'merit', 'program', 'it', 'programmer']))
print('programmerit:', break_string('programmerit', ['pro', 'gram', 'merit', 'program', 'it', 'programmer']))
print('programlala:', break_string('programlala', ['pro', 'gram', 'merit', 'program', 'it', 'programmer']))
print('proletarian:', break_string('proletarian', ['pro', 'gram', 'merit', 'program', 'it', 'programmer']))