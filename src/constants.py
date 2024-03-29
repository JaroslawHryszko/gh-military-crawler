import mimetypes
from pathlib import Path
from typing import List

# TODO change those into frozen counterparts
# from frozenlist import FrozenList


MIN_PROBABILITY_TO_ACCEPT: float = 0.4
ROOT_PROJECT_PATH = Path(__file__).parent.parent


def get_extensions_for_type(general_type: str):
    for ext in mimetypes.types_map:
        if mimetypes.types_map[ext].split("/")[0] == general_type:
            yield ext


# https://stackoverflow.com/a/4292127
mimetypes.init()

image_extensions = list(get_extensions_for_type("image"))
invalid_extensions: List[str] = [".dll", ".exe", ".paa", ".p3d"]

# TODO add more languages or split them
programming_languages: List[str] = ["Assembly", "Ada", "C++", "C", "Rust"]

cyryllic_languages: List[str] = [
    "be",
    "bg",
    "kk",
    "ky",
    "mk",
    "sr",
    "ru",
    "tg",
    "tk",
    "uk",
    "uz",
]
# pylint: disable=line-too-long
language_short_name = {
    "aa": "Afar",
    "ab": "Abkhazian",
    "af": "Afrikaans",
    "ak": "Akan",
    "sq": "Albanian",
    "am": "Amharic",
    "ar": "Arabic",
    "an": "Aragonese",
    "hy": "Armenian",
    "as": "Assamese",
    "av": "Avaric",
    "ae": "Avestan",
    "ay": "Aymara",
    "az": "Azerbaijani",
    "ba": "Bashkir",
    "bm": "Bambara",
    "eu": "Basque",
    "be": "Belarusian",
    "bn": "Bengali",
    "bh": "Bihari languages",
    "bi": "Bislama",
    "bo": "Tibetan",
    "bs": "Bosnian",
    "br": "Breton",
    "bg": "Bulgarian",
    "my": "Burmese",
    "ca": "Catalan; Valencian",
    "cs": "Czech",
    "ch": "Chamorro",
    "ce": "Chechen",
    "zh": "Chinese",
    "cu": "Church Slavic; Old Slavonic; Church Slavonic; Old Bulgarian; Old Church Slavonic",
    "cv": "Chuvash",
    "kw": "Cornish",
    "co": "Corsican",
    "cr": "Cree",
    "cy": "Welsh",
    "da": "Danish",
    "de": "German",
    "dv": "Divehi; Dhivehi; Maldivian",
    "nl": "Dutch; Flemish",
    "dz": "Dzongkha",
    "el": "Greek-Modern (1453-)",
    "en": "English",
    "eo": "Esperanto",
    "et": "Estonian",
    "ee": "Ewe",
    "fo": "Faroese",
    "fa": "Persian",
    "fj": "Fijian",
    "fi": "Finnish",
    "fr": "French",
    "fy": "Western Frisian",
    "ff": "Fulah",
    "Ga": "Georgian",
    "gd": "Gaelic; Scottish Gaelic",
    "ga": "Irish",
    "gl": "Galician",
    "gv": "Manx",
    "gn": "Guarani",
    "gu": "Gujarati",
    "ht": "Haitian; Haitian Creole",
    "ha": "Hausa",
    "he": "Hebrew",
    "hz": "Herero",
    "hi": "Hindi",
    "ho": "Hiri Motu",
    "hr": "Croatian",
    "hu": "Hungarian",
    "ig": "Igbo",
    "is": "Icelandic",
    "io": "Ido",
    "ii": "Sichuan Yi; Nuosu",
    "iu": "Inuktitut",
    "ie": "Interlingue; Occidental",
    "ia": "Interlingua (International Auxiliary Language Association)",
    "id": "Indonesian",
    "ik": "Inupiaq",
    "it": "Italian",
    "jv": "Javanese",
    "ja": "Japanese",
    "kl": "Kalaallisut; Greenlandic",
    "kn": "Kannada",
    "ks": "Kashmiri",
    "ka": "Georgian",
    "kr": "Kanuri",
    "kk": "Kazakh",
    "km": "Central Khmer",
    "ki": "Kikuyu; Gikuyu",
    "rw": "Kinyarwanda",
    "ky": "Kirghiz; Kyrgyz",
    "kv": "Komi",
    "kg": "Kongo",
    "ko": "Korean",
    "kj": "Kuanyama; Kwanyama",
    "ku": "Kurdish",
    "lo": "Lao",
    "la": "Latin",
    "lv": "Latvian",
    "li": "Limburgan; Limburger; Limburgish",
    "ln": "Lingala",
    "lt": "Lithuanian",
    "lb": "Luxembourgish; Letzeburgesch",
    "lu": "Luba-Katanga",
    "lg": "Ganda",
    "mk": "Macedonian",
    "mh": "Marshallese",
    "ml": "Malayalam",
    "mi": "Maori",
    "mr": "Marathi",
    "ms": "Malay",
    "Mi": "Micmac",
    "mg": "Malagasy",
    "mt": "Maltese",
    "mn": "Mongolian",
    "na": "Nauru",
    "nv": "Navajo; Navaho",
    "nr": "Ndebele-South; South Ndebele",
    "nd": "Ndebele-North; North Ndebele",
    "ng": "Ndonga",
    "ne": "Nepali",
    "nn": "Norwegian Nynorsk; Nynorsk:Norwegian",
    "nb": "Bokmål-Norwegian; Norwegian Bokmål",
    "no": "Norwegian",
    "oc": "Occitan (post 1500)",
    "oj": "Ojibwa",
    "or": "Oriya",
    "om": "Oromo",
    "os": "Ossetian; Ossetic",
    "pa": "Panjabi; Punjabi",
    "pi": "Pali",
    "pl": "Polish",
    "pt": "Portuguese",
    "ps": "Pushto; Pashto",
    "qu": "Quechua",
    "rm": "Romansh",
    "ro": "Romanian; Moldavian; Moldovan",
    "rn": "Rundi",
    "ru": "Russian",
    "sg": "Sango",
    "sa": "Sanskrit",
    "si": "Sinhala; Sinhalese",
    "sk": "Slovak",
    "sl": "Slovenian",
    "se": "Northern Sami",
    "sm": "Samoan",
    "sn": "Shona",
    "sd": "Sindhi",
    "so": "Somali",
    "st": "Sotho-Southern",
    "es": "Spanish; Castilian",
    "sc": "Sardinian",
    "sr": "Serbian",
    "ss": "Swati",
    "su": "Sundanese",
    "sw": "Swahili",
    "sv": "Swedish",
    "ty": "Tahitian",
    "ta": "Tamil",
    "tt": "Tatar",
    "te": "Telugu",
    "tg": "Tajik",
    "tl": "Tagalog",
    "th": "Thai",
    "ti": "Tigrinya",
    "to": "Tonga (Tonga Islands)",
    "tn": "Tswana",
    "ts": "Tsonga",
    "tk": "Turkmen",
    "tr": "Turkish",
    "tw": "Twi",
    "ug": "Uighur; Uyghur",
    "uk": "Ukrainian",
    "ur": "Urdu",
    "uz": "Uzbek",
    "ve": "Venda",
    "vi": "Vietnamese",
    "vo": "Volapük",
    "wa": "Walloon",
    "wo": "Wolof",
    "xh": "Xhosa",
    "yi": "Yiddish",
    "yo": "Yoruba",
    "za": "Zhuang; Chuang",
    "zu": "Zulu",
}
