import pandas as pd

# Read The quran file
file = open('quran-simple-clean.txt', 'r', encoding='utf-8')
quranList = file.read().splitlines()
file.close()
###
# Read the file content #
###
# print(quranList)

###
# Put the Ayat in Dataframe #
###
df_ayat = pd.DataFrame(quranList, columns=['aya'])
# print(df_ayat)


###
# Count the lenght of ayayte #
###
df_ayat['aye_len'] = df_ayat.aya.apply(lambda x: len(x))
print(df_ayat)