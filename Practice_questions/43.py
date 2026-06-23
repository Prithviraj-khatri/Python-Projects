# Complete the solution so that the function will break up camel casing, using a space between words.

#Example
#"camelCasing"  =>  "camel Casing"
#"identifier"   =>  "identifier"
# ""             =>  ""

def solution(s):
    result = ""

    for ch in s:
        if ch.isupper():
            result += " "
        result += ch

    return result

