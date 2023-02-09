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
print(df_ayat)
