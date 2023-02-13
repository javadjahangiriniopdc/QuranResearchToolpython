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
df_ayat['aya_len'] = df_ayat.aya.apply(lambda x: len(x))
# print(df_ayat)

###
# Longset of aya in Qurab #
###
print(max(df_ayat.aya_len))
print(df_ayat.loc[df_ayat.aya_len == max(df_ayat.aya_len)])
print(df_ayat.loc[df_ayat.aya_len == max(df_ayat.aya_len)].values)

###
# Shortest of aya in Quran #
###
# print(min(df_ayat.aya_len))
# print(df_ayat.loc[df_ayat.aya_len == min(df_ayat.aya_len)])
# print(df_ayat.loc[df_ayat.aya_len == min(df_ayat.aya_len)].values)