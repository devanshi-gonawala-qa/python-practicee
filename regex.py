# Regex
# Character    meaning
# . -> any character(except newline) 
# \D -> Not a digit
# \d - digit (0-9)
# \w - Alphanumeric or underscore
# \W - Not alphanumeric
# \s => white space
# \not whitespace
# Anchors -> ^ Start with the anchor, end of the $, and \b that word includes spereatly in the sentneces

# 1. ^abc => match if string starts with abc
# "abc 123" - correct
# ""abcefg- correct
# "abc is in the start"- correct
# Doesn't match "X abc Y" , "123 abc", "the abc"

# 2. abc$ - the string should end with abc
# Correct => "123 abc" , "xyzabc" , "ending with abc", "abc abc"
# Not match => "abc 123", "abcc" , "x abc "

# 3. \b word \b => matches the exact word with word boundries
# "[a-z]" [A-z][0-9]_" non word characters " " , !,#
# "this is a word" , "Word,", "the word is here" , "word"
# non match => "password", "sword", "wording"

# Characters set and range
# [abc] -> matches a,b,c -> anyone
# [a-z] => matches any one lower case character
# [0-9] => matches any one digit
# [^a-z] => not lower case

# Pattern
#  Correct -> "App" , "Bob" , "Ape"
# Non correct => "APp" , "B1"

# Quantifiers
# Symbol        Meaning
# *     -        0 or more
# +     -        1 or more
# ?     -        0 or 1
# {3}   -        Exactly 3 character
# {2,4} -        Between 2 and 4 character
# ()    -        group

# 1). (ab)+
# correct - ab, abab,ababab, abx, xab
# Non correct a

# 2) abc+
# abc -> c can repeat 1 or more time - abcccc

# 3) ([\._]?\w+)* - this is group \. escape character
# [\.-]? => match zero or 1 occuraance a of "." or "-""
# \w => alphanumer, + -> 1 or more
# [\.-]?\w+ => optionaly . or - followed by alphanumeric one or more times
# ([\.-]?\w+)* -> group can happen o or more times

# => or => helps in making choice
# Find pattern for full name with prefix
# \b(Mr/Mrs?ms).\.?\s[A-Z][a-z]+\b
# Coorect => "Mr.John" , "Hello Mr.John"
# Not correct => "mr.John" => m is lower caps , "Mr. 123434"