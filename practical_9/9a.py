# Install first (run once in terminal)
# pip install fuzzywuzzy python-Levenshtein

from fuzzywuzzy import fuzz, process

s1 = "I love fuzzysforfuzzys"
s2 = "I am loving fuzzysforfuzzys"

print("Ratio:", fuzz.ratio(s1, s2))
print("Partial:", fuzz.partial_ratio(s1, s2))
print("Token Sort:", fuzz.token_sort_ratio(s1, s2))
print("Token Set:", fuzz.token_set_ratio(s1, s2))
print("WRatio:", fuzz.WRatio(s1, s2))

query = "fuzzys for fuzzys"
choices = ["fuzzy for fuzzy", "fuzzy fuzzy", "g. for fuzzys"]

print("Best match:", process.extractOne(query, choices))

