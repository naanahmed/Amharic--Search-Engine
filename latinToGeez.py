def convertBack(s):
    mapping = {'Hä': 'ሀ', 'Hu': 'ሁ', 'Hi': 'ሂ', 'ሃ': 'Ha', 'He': 'ሄ', 'H': 'ህ', 'Ho': 'ሆ',
               'Lä': 'ለ', 'Lu': 'ሉ', 'Li': 'ሊ', 'La': 'ላ', 'Le': 'ሌ', 'L': 'ል', 'Lo': 'ሎ',
               'Mä': 'መ', 'Mu': 'ሙ', 'Mi': 'ሚ', 'Ma': 'ማ', 'Me': 'ሜ', 'M': 'ም', 'Mo': 'ሞ',
               'Sä': 'ሠ', 'Su': 'ሡ', 'Si': 'ሢ', 'Sa': 'ሣ', 'Se': 'ሤ', 'S': 'ሥ', 'So': 'ሦ',
               'Rä': 'ረ', 'Ru': 'ሩ', 'Ri': 'ሪ', 'Ra': 'ራ', 'Re': 'ሬ', 'R': 'ር', 'Ro': 'ሮ',
               'Ŝä': 'ሸ', 'Ŝu': 'ሹ', 'Ŝi': 'ሺ', 'Ŝa': 'ሻ', 'Ŝe': 'ሼ', 'Ŝ': 'ሽ', 'Ŝo': 'ሾ',
               'Qä': 'ቀ', 'Qu': 'ቁ', 'Qi': 'ቂ', 'Qa': 'ቃ', 'Qe': 'ቄ', 'Q': 'ቅ', 'Qo': 'ቆ',
               'Bä': 'በ', 'Bu': 'ቡ', 'Bi': 'ቢ', 'Ba': 'ባ', 'Be': 'ቤ', 'B': 'ብ', 'Bo': 'ቦ',
               'Tä': 'ተ', 'Tu': 'ቱ', 'Ti': 'ቲ', 'Ta': 'ታ', 'Te': 'ቴ', 'T': 'ት', 'To': 'ቶ',
               'Čä': 'ቸ', 'Ču': 'ቹ', 'Či': 'ቺ', 'Ča': 'ቻ', 'Če': 'ቼ', 'Č': 'ች', 'Čo': 'ቾ',
               'Nä': 'ነ', 'Nu': 'ኑ', 'Ni': 'ኒ', 'Na': 'ና', 'Ne': 'ኔ', 'N': 'ን', 'No': 'ኖ',
               'Ñä': 'ኘ', 'Ñu': 'ኙ', 'Ñi': 'ኚ', 'Ña': 'ኛ', 'Ñe': 'ኜ', 'Ñ': 'ኝ', 'Ño': 'ኞ',
               'Ä': 'አ', 'U': 'ኡ', 'I': 'ኢ', 'A': 'ኣ', 'É': 'ኤ', 'E': 'እ', 'O': 'ኦ',
               'Kä': 'ከ', 'Ku': 'ኩ', 'Ki': 'ኪ', 'Ka': 'ካ', 'Ke': 'ኬ', 'K': 'ክ', 'Ko': 'ኮ',
               'Xä': 'ኸ', 'Xu': 'ኹ', 'Xi': 'ኺ', 'Xa': 'ኻ', 'Xe': 'ኼ', 'X': 'ኽ', 'Xo': 'ኾ',
               'Wä': 'ወ', 'Wu': 'ዉ', 'Wi': 'ዊ', 'Wa': 'ዋ', 'We': 'ዌ', 'W': 'ው', 'Wo': 'ዎ',
               'Aä': 'ዐ', 'Au': 'ዑ', 'Ai': 'ዒ', 'Aā': 'ዓ', 'Aé': 'ዔ', 'Aa': 'ዕ', 'Ao': 'ዖ',
               'Zä': 'ዘ', 'Zu': 'ዙ', 'Zi': 'ዚ', 'Za': 'ዛ', 'Ze': 'ዜ', 'Z': 'ዝ', 'Zo': 'ዞ',
               'Žä': 'ዠ', 'Žu': 'ዡ', 'Ži': 'ዢ', 'Ža': 'ዣ', 'Žw': 'ዤ', 'Ž': 'ዥ', 'Žo': 'ዦ',
               'Yä': 'የ', 'Yu': 'ዩ', 'Yi': 'ዪ', 'Ya': 'ያ', 'Ye': 'ዬ', 'Y': 'ይ', 'Yo': 'ዮ',
               'Dä': 'ደ', 'Du': 'ዱ', 'Di': 'ዲ', 'Da': 'ዳ', 'De': 'ዴ', 'D': 'ድ', 'Do': 'ዶ',
               'Ğä': 'ጀ', 'Ğu': 'ጁ', 'Ği': 'ጂ', 'Ğa': 'ጃ', 'Ğe': 'ጄ', 'Ğ': 'ጅ', 'Ğo': 'ጆ',
               'Gä': 'ገ', 'Gu': 'ጉ', 'Gi': 'ጊ', 'Ga': 'ጋ', 'Ge': 'ጌ', 'G': 'ግ', 'Go': 'ጎ',
               'Ṭä': 'ጠ', 'Ṭu': 'ጡ', 'Ṭi': 'ጢ', 'Ṭa': 'ጣ', 'Ṭe': 'ጤ', 'Ṭ': 'ጥ', 'Ṭo': 'ጦ',
               'Ċä': 'ጨ', 'Ċu': 'ጩ', 'Ċi': 'ጪ', 'Ċa': 'ጫ', 'Ċe': 'ጬ', 'Ċ': 'ጭ', 'Ċo': 'ጮ',
               'Ṗä': 'ጰ', 'Ṗu': 'ጱ', 'Ṗi': 'ጲ', 'Ṗa': 'ጳ', 'Ṗ': 'ጵ', 'Ṗo': 'ጶ',
               'Ṣä': 'ጸ', 'Ṣu': 'ጹ', 'Ṣi': 'ጺ', 'Ṣa': 'ጻ', 'Ṣe': 'ጼ', 'Ṣ': 'ጽ', 'Ṣo': 'ጾ',
               'Ṡä': 'ፀ', 'Ṡu': 'ፁ', 'Ṡi': 'ፂ', 'Ṡa': 'ፃ', 'Ṡe': 'ፄ', 'Ṡ': 'ፅ', 'Ṡo': 'ፆ',
               'Fä': 'ፈ', 'Fu': 'ፉ', 'Fi': 'ፊ', 'Fa': 'ፋ', 'Fe': 'ፌ', 'F': 'ፍ', 'Fo': 'ፎ',
               'Pä': 'ፐ', 'Pu': 'ፑ', 'Pi': 'ፒ', 'Pa': 'ፓ', 'Pe': 'ፔ', 'P': 'ፕ', 'Po': 'ፖ',
               'Vä': 'ቨ', 'Vu': 'ቩ', 'Vi': 'ቪ', 'Va': 'ቫ', 'Ve': 'ቬ', 'V': 'ቭ', 'Vo': 'ቮ'
               }

    converted_to_geez = ''
    i = 0
    while i < len(s):
        pair = s[i:i + 2]
        if pair in mapping:
            converted_to_geez += mapping[pair]
            i += 2
        else:
            converted_to_geez += mapping.get(s[i], s[i])
            i += 1

    return converted_to_geez
