def all_variants(text):
    for i in range(len(text)):
        for j in range(i, len(text)):
            # yield text[i:j+1]

            yield text[i:(j+1)]

a = all_variants("abc")

for y in a:
    print(y)
