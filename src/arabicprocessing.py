#functions dedicated to Arabic language.
import string
def definite_arabic(text):
  """it identifies and extracts words that begin with the Arabic definite article 'ال' (alef lam) and its variations. This function takes a single parameter: the text to analyze. It returns the total count of words that start with the Arabic definite article and prints a list of these words found within the given text. The function ignores punctuation and digits."""
  arabic_punctuation="،؛؟:•\"“”'()[]{}<>ـ"
  definite_arabic_count=0
  definite_arabic_list=[]
  arabic_particals=["ال","بال","كال","فال","وال", "تال"]
  splitted_text=text.split()
  for i in splitted_text:
    i=i.strip(string.punctuation+string.digits+arabic_punctuation)
    for p in arabic_particals:
      if len(i)>len(p) and i[:len(p)]==p:
        definite_arabic_list.append(i)
        definite_arabic_count+=1
  print(f"الكلمات التي وجدناها في النص تبدأ ب\"ال\" هي: \"{', '.join(definite_arabic_list)}\"، وعددها هو: ")
  return definite_arabic_count
def feminine_arabic_sign(text):
  """It identifies and extracts words that end with the Arabic feminine sign 'ة' (teh marbyuta). This function takes a single parameter: the text to analyze. It returns the total count of words that end with the Arabic feminine sign and prints a list of these words found in the given text. it ignores punctuation and digits."""
  arabic_punctuation="،؛؟:•\"“”'()[]{}<>ـ"
  feminine_count=0
  feminine_arabic_word_list=[]
  splitted_text=text.split()
  for i in splitted_text:
    i=i.strip(string.punctuation+string.digits+arabic_punctuation)
    if i[-1]=="ة":
      feminine_arabic_word_list.append(i)
      feminine_count+=1
  print(f"الكلمات الموجودة في هذا النص التي تنتهي بالتاء المربوطة هي: \"{', '.join(feminine_arabic_word_list)}\"، وعددها هو: ")
  return feminine_count
def feminine_plural_arabic(text, exclusion):
  """It identifies and extracts words that end with common Arabic feminine plural suffixes within the given text. This function takes two parameters: the text to analyze and a list of words to exclude from the analysis. In case you do not have any exceptions to exclude, you can leave its square brackets empty. It returns the total count of words that end with common Arabic feminine plural suffixes and prints a list of these words found within the given text. It ignores punctuation and digits."""
  if not type(exclusion)==list:
    exclusion=[exclusion]
  arabic_punctuation="،؛؟:•\"“”'()[]{}<>ـ"
  feminine_plural_words=[]
  feminine_plural_list=["ات", "اتهم", "اتهن", "اتكن", "اتكم", "اتكما", "اتهما", "اتنا", "اتك", "اته", "اتها", "اتي"]
  feminine_plural_count=0
  splitted_text=text.split()
  for i in splitted_text:
    i=i.strip(string.punctuation+string.digits+arabic_punctuation)
    if i!="اللاتي" and i not in exclusion:
      for s in feminine_plural_list:
        if len(i)>len(s) and i[-len(s):]==s:
          feminine_plural_words.append(i)
          feminine_plural_count+=1
  print(f"الكلمات التي تنتهي بالألف والتاء في النص الذي وضعته هي \"{', '.join(feminine_plural_words)}\"، وإجمالي عددها هو: ")
  return feminine_plural_count
def diacritics_removal(text):
  """It displays the Arabic text free of any diacritics. This function takes a single parameter: the text from which to remove diacritics. It returns a new string with all diacritics removed."""
  diacritics="ًٌٍَُِّْٰٓـ"
  clean_text=""
  for i in text:
    if i not in diacritics:
      clean_text+=i
  return clean_text
def singular_extended_arabic(text, user_exceptions):
  """It finds singular extended Arabic nouns ending with 'اء' (alif and hamza) in the given text, excluding specified exceptions. It takes two parameters; the first one is the text string, and the second one is a list of user-defined exceptions. In case you do not have any exceptions to exclude, you can leave its square brackets empty. It returns the count of singular extended Arabic words found in the text, excluding common and user-defined exceptions. The function strips punctuation, digits, and diacritics from the words before processing."""
  if not type(user_exceptions)==list:
    user_exceptions=[user_exceptions]
  extended_list=[]
  exclusions_list=["شاء", "جاء", "ساء", "باء", "تاء", "ثاء", "حاء", "خاء", "راء", "طاء", "ظاء", "فاء", "هاء", "ياء", "هؤلاء", "ماء", "داء"]
  extended_count=0
  split_text=text.split()
  diacritics="ًٌٍَُِّْٰٓـ"
  arabic_punctuation="،؛؟:•\"“”'()[]{}<>ـ"
  for i in split_text:
    i=i.strip(string.punctuation+string.digits+arabic_punctuation+diacritics)
    if i not in exclusions_list and i not in user_exceptions and i[-2:]=="اء":
      extended_list.append(i)
      extended_count+=1
  print(f"الأسماء الممدودة المفردة الموجودة في هذا النص هي: \"{', '.join(extended_list)}\"، وعددها هو: ")
  return extended_count