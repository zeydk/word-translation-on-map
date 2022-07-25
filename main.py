import pandas as pd
import geopandas as gp
from googletrans import Translator
translator = Translator()
from matplotlib import pyplot as plt

europe = gp.read_file("Europe.shp")
europe = europe[europe["NAME"]!="Andorra"]
europe = europe[europe["NAME"]!="Gibraltar (UK)"]
europe = europe[europe["NAME"]!="Isle of Man (UK)"]
europe = europe[europe["NAME"]!="Jersey (UK)"]
europe = europe[europe["NAME"]!="San Marino"]	
europe = europe[europe["NAME"]!="Faeroe Islands (Denmark)"]
europe = europe[europe["NAME"]!="Jan Mayen (Norway)"]
europe = europe[europe["NAME"]!="Svalbard (Norway)"]
europe = europe[europe["NAME"]!="Guernsey (UK)"]
europe = europe[europe["NAME"]!="Monaco"]
europe = europe.reset_index()
europe["src_id"] = ["sq", "de", "fr", "bs", "hr", "cs", "da", "et", "fi", "fr", "de", "el", "hu", "ga", "it", "lv", "de", "lt", "lb", "mk", "mt", "sr", "nl", "no", "pl", "pt", "sr", "sk", "sl", "es", "sv", "fr", "en", "hy", "az", "be", "bg", "ka", "is", "ro", "ro", "tr", "uk", "ru"]
europe["word"] = 0
europe.drop('index', inplace=True, axis=1)
langdic = {'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian', 'az': 'azerbaijani', 'eu': 'basque','be': 'belarusian', 'bn': 'bengali', 'bs': 'bosnian', 'bg': 'bulgarian', 'ca': 'catalan', 'ceb': 'cebuano', 'ny': 'chichewa', 'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)', 'co': 'corsican', 'hr': 'croatian', 'cs': 'czech', 'da': 'danish', 'nl': 'dutch', 'en': 'english', 'eo': 'esperanto', 'et': 'estonian', 'tl': 'filipino', 'fi': 'finnish', 'fr': 'french', 'fy': 'frisian', 'gl': 'galician', 'ka': 'georgian', 'de': 'german', 'el': 'greek', 'gu': 'gujarati', 'ht': 'haitian creole', 'ha': 'hausa', 'haw': 'hawaiian', 'iw': 'hebrew', 'he': 'hebrew', 'hi': 'hindi', 'hmn': 'hmong', 'hu': 'hungarian', 'is': 'icelandic', 'ig': 'igbo', 'id': 'indonesian', 'ga': 'irish', 'it': 'italian', 'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh', 'km': 'khmer', 'ko': 'korean', 'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz', 'lo': 'lao', 'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian', 'lb': 'luxembourgish', 'mk': 'macedonian', 'mg': 'malagasy', 'ms': 'malay', 'ml': 'malayalam', 'mt': 'maltese', 'mi': 'maori', 'mr': 'marathi', 'mn': 'mongolian', 'my': 'myanmar (burmese)', 'ne': 'nepali', 'no': 'norwegian', 'or': 'odia', 'ps': 'pashto', 'fa': 'persian', 'pl': 'polish', 'pt': 'portuguese', 'pa': 'punjabi', 'ro': 'romanian', 'ru': 'russian', 'sm': 'samoan', 'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho', 'sn': 'shona', 'sd': 'sindhi', 'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali', 'es': 'spanish', 'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish', 'tg': 'tajik', 'ta': 'tamil', 'te': 'telugu', 'th': 'thai', 'tr': 'turkish', 'uk': 'ukrainian', 'ur': 'urdu', 'ug': 'uyghur', 'uz': 'uzbek', 'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu'}
langdic = list(langdic.values())

ifenglish = input('Do you want to enter a word in English? (Y/N)\n')
if ifenglish.strip().lower() == 'y':
       input_word = input('Please enter a word in English\n')
       input_lang = "en"
else:
    input_lang = input('What language is the word?\n')
    if input_lang.strip().lower() == 'afrikaans':
         input_lang == 'af' 
    elif input_lang.strip().lower() == 'albanian':
         input_lang == 'sq' 
    elif input_lang.strip().lower() == 'amharic':
         input_lang == 'am' 
    elif input_lang.strip().lower() == 'arabic':
         input_lang == 'ar' 
    elif input_lang.strip().lower() == 'armenian':
         input_lang == 'hy' 
    elif input_lang.strip().lower() == 'azerbaijani':
         input_lang == 'az' 
    elif input_lang.strip().lower() == 'basque':
         input_lang == 'eu' 
    elif input_lang.strip().lower() == 'belarusian':
         input_lang == 'be' 
    elif input_lang.strip().lower() == 'bengali':
         input_lang == 'bn' 
    elif input_lang.strip().lower() == 'bosnian':
         input_lang == 'bs' 
    elif input_lang.strip().lower() == 'bulgarian':
         input_lang == 'bg' 
    elif input_lang.strip().lower() == 'catalan':
         input_lang == 'ca' 
    elif input_lang.strip().lower() == 'cebuano':
         input_lang == 'ceb' 
    elif input_lang.strip().lower() == 'chichewa':
         input_lang == 'ny' 
    elif input_lang.strip().lower() == 'chinese (simplified)':
         input_lang == 'zh-cn' 
    elif input_lang.strip().lower() == 'chinese (traditional)':
         input_lang == 'zh-tw' 
    elif input_lang.strip().lower() == 'corsican':
         input_lang == 'co' 
    elif input_lang.strip().lower() == 'croatian':
         input_lang == 'hr' 
    elif input_lang.strip().lower() == 'czech':
         input_lang == 'cs' 
    elif input_lang.strip().lower() == 'danish':
         input_lang == 'da' 
    elif input_lang.strip().lower() == 'dutch':
         input_lang == 'nl' 
    elif input_lang.strip().lower() == 'english':
         input_lang == 'en' 
    elif input_lang.strip().lower() == 'esperanto':
         input_lang == 'eo' 
    elif input_lang.strip().lower() == 'estonian':
         input_lang == 'et' 
    elif input_lang.strip().lower() == 'filipino':
         input_lang == 'tl' 
    elif input_lang.strip().lower() == 'finnish':
         input_lang == 'fi' 
    elif input_lang.strip().lower() == 'french':
         input_lang == 'fr' 
    elif input_lang.strip().lower() == 'frisian':
         input_lang == 'fy' 
    elif input_lang.strip().lower() == 'galician':
         input_lang == 'gl' 
    elif input_lang.strip().lower() == 'georgian':
         input_lang == 'ka' 
    elif input_lang.strip().lower() == 'german':
         input_lang == 'de' 
    elif input_lang.strip().lower() == 'greek':
         input_lang == 'el' 
    elif input_lang.strip().lower() == 'gujarati':
         input_lang == 'gu' 
    elif input_lang.strip().lower() == 'haitian creole':
         input_lang == 'ht' 
    elif input_lang.strip().lower() == 'hausa':
         input_lang == 'ha' 
    elif input_lang.strip().lower() == 'hawaiian':
         input_lang == 'haw' 
    elif input_lang.strip().lower() == 'hebrew':
         input_lang == 'iw' 
    elif input_lang.strip().lower() == 'hebrew':
         input_lang == 'he' 
    elif input_lang.strip().lower() == 'hindi':
         input_lang == 'hi' 
    elif input_lang.strip().lower() == 'hmong':
         input_lang == 'hmn' 
    elif input_lang.strip().lower() == 'hungarian':
         input_lang == 'hu' 
    elif input_lang.strip().lower() == 'icelandic':
         input_lang == 'is' 
    elif input_lang.strip().lower() == 'igbo':
         input_lang == 'ig' 
    elif input_lang.strip().lower() == 'indonesian':
         input_lang == 'id' 
    elif input_lang.strip().lower() == 'irish':
         input_lang == 'ga' 
    elif input_lang.strip().lower() == 'italian':
         input_lang == 'it' 
    elif input_lang.strip().lower() == 'japanese':
         input_lang == 'ja' 
    elif input_lang.strip().lower() == 'javanese':
         input_lang == 'jw' 
    elif input_lang.strip().lower() == 'kannada':
         input_lang == 'kn' 
    elif input_lang.strip().lower() == 'kazakh':
         input_lang == 'kk' 
    elif input_lang.strip().lower() == 'khmer':
         input_lang == 'km' 
    elif input_lang.strip().lower() == 'korean':
         input_lang == 'ko' 
    elif input_lang.strip().lower() == 'kurdish (kurmanji)':
         input_lang == 'ku' 
    elif input_lang.strip().lower() == 'kyrgyz':
         input_lang == 'ky' 
    elif input_lang.strip().lower() == 'lao':
         input_lang == 'lo' 
    elif input_lang.strip().lower() == 'latin':
         input_lang == 'la' 
    elif input_lang.strip().lower() == 'latvian':
         input_lang == 'lv' 
    elif input_lang.strip().lower() == 'lithuanian':
         input_lang == 'lt' 
    elif input_lang.strip().lower() == 'luxembourgish':
         input_lang == 'lb' 
    elif input_lang.strip().lower() == 'macedonian':
         input_lang == 'mk' 
    elif input_lang.strip().lower() == 'malagasy':
         input_lang == 'mg' 
    elif input_lang.strip().lower() == 'malay':
         input_lang == 'ms' 
    elif input_lang.strip().lower() == 'malayalam':
         input_lang == 'ml'
    elif input_lang.strip().lower() == 'maltese':
         input_lang == 'mt' 
    elif input_lang.strip().lower() == 'maori':
         input_lang == 'mi' 
    elif input_lang.strip().lower() == 'marathi':
         input_lang == 'mr' 
    elif input_lang.strip().lower() == 'mongolian':
         input_lang == 'mn' 
    elif input_lang.strip().lower() == 'myanmar (burmese)':
         input_lang == 'my' 
    elif input_lang.strip().lower() == 'nepali':
         input_lang == 'ne' 
    elif input_lang.strip().lower() == 'norwegian':
         input_lang == 'no' 
    elif input_lang.strip().lower() == 'odia':
         input_lang == 'or' 
    elif input_lang.strip().lower() == 'pashto':
         input_lang == 'ps' 
    elif input_lang.strip().lower() == 'persian':
         input_lang == 'fa' 
    elif input_lang.strip().lower() == 'polish':
         input_lang == 'pl' 
    elif input_lang.strip().lower() == 'portuguese':
         input_lang == 'pt' 
    elif input_lang.strip().lower() == 'punjabi':
         input_lang == 'pa' 
    elif input_lang.strip().lower() == 'romanian':
         input_lang == 'ro' 
    elif input_lang.strip().lower() == 'russian':
         input_lang == 'ru' 
    elif input_lang.strip().lower() == 'samoan':
         input_lang == 'sm' 
    elif input_lang.strip().lower() == 'scots gaelic':
         input_lang == 'gd' 
    elif input_lang.strip().lower() == 'serbian':
         input_lang == 'sr' 
    elif input_lang.strip().lower() == 'sesotho':
         input_lang == 'st' 
    elif input_lang.strip().lower() == 'shona': 
         input_lang == 'sn' 
    elif input_lang.strip().lower() == 'sindhi':
         input_lang == 'sd' 
    elif input_lang.strip().lower() == 'sinhala':
         input_lang == 'si' 
    elif input_lang.strip().lower() == 'slovak':
         input_lang == 'sk' 
    elif input_lang.strip().lower() == 'slovenian':
         input_lang == 'sl' 
    elif input_lang.strip().lower() == 'somali':
         input_lang == 'so' 
    elif input_lang.strip().lower() == 'spanish':
         input_lang == 'es' 
    elif input_lang.strip().lower() == 'sundanese':
         input_lang == 'su' 
    elif input_lang.strip().lower() == 'swahili':
         input_lang == 'sw' 
    elif input_lang.strip().lower() == 'swedish':
         input_lang == 'sv' 
    elif input_lang.strip().lower() == 'tajik':
         input_lang == 'tg' 
    elif input_lang.strip().lower() == 'tamil':
         input_lang == 'ta' 
    elif input_lang.strip().lower() == 'telugu':
         input_lang == 'te' 
    elif input_lang.strip().lower() == 'thai':
         input_lang == 'th' 
    elif input_lang.strip().lower() == 'turkish':
         input_lang == 'tr'
    elif input_lang.strip().lower() == 'ukrainian':
         input_lang == 'uk' 
    elif input_lang.strip().lower() == 'urdu':
         input_lang == 'ur' 
    elif input_lang.strip().lower() == 'uyghur':
         input_lang == 'ug' 
    elif input_lang.strip().lower() == 'uzbek':
         input_lang == 'uz' 
    elif input_lang.strip().lower() == 'vietnamese':
         input_lang == 'vi' 
    elif input_lang.strip().lower() == 'welsh':
         input_lang == 'cy' 
    elif input_lang.strip().lower() == 'xhosa':
         input_lang == 'xh' 
    elif input_lang.strip().lower() == 'yiddish':
         input_lang == 'yi' 
    elif input_lang.strip().lower() == 'yoruba':
         input_lang == 'yo' 
    elif input_lang.strip().lower() == 'zulu':
         input_lang == 'zu' 
    input_word = input('Please enter the word in '+ input_lang + '\n')


for i in range(0, len(europe)):
    europe["word"][i] = translator.translate(text = input_word, src= input_lang, dest=europe["src_id"][i]).text
europe_points = europe.copy()
europe_points["center"] = europe_points["geometry"].centroid
europe_points.set_geometry("center", inplace = True)

import adjustText as aT
ax = europe.plot(figsize = (30, 30), cmap="Pastel1", edgecolor='white')
texts = []

for x, y, label in zip(europe_points.center.x-2, europe_points.center.y, europe_points["word"]):
   texts.append(plt.text(x, y, label, fontsize = 12, bbox={'facecolor': 'white', 'alpha':0.5, 'pad': 1, 'edgecolor':'none'}))


ax.set_axis_off()
plt.savefig(input_word+'.jpg')