#these functions are dedicated to English language only.
import string
import re
def vowel_consonant_count(text):
  """It counts the total number of vowels and consonants in the given text. This function takes a single parameter: the text to analyze. It returns a tuple containing the total count of vowels and consonants. The function is case-insensitive and only considers alphabetic characters."""
  vowel_characters="aeiou"
  vowel_count=0
  consonant_count=0
  for i in text:
    if i in vowel_characters:
      vowel_count+=1
    else:
      consonant_count+=1
  return vowel_count, consonant_count
def upper_lower_count(text):
  """It counts the total number of uppercase and lowercase letters in the given text. This function takes a single parameter: the text to analyze. It returns a tuple containing the total count of uppercase and lowercase letters. The function uses the ASCII values to determine the case of each letter."""
  upper_case=0
  lower_case=0
  for i in text:
    if ord(i)>=65 and ord(i)<=90:
      upper_case+=1
    elif ord(i)>=97 and ord(i)<=122:
      lower_case+=1
  return upper_case, lower_case
def ed_ing_count(text,exclusions):
  """It counts the total number of words ending with 'ed' and 'ing' in the given text, excluding specified words. This function takes two parameters: the text to analyze and a list of words to exclude from the analysis. In case you do not have any exceptions to exclude, you can leave its square brackets empty. It returns a tuple containing the total count of words ending with 'ed' and 'ing'. The function is case-insensitive and ignores punctuation and digits."""
  if not type(exclusions)==list:
    exclusions=[exclusions]
  ed_words_list=[]
  ing_words_list=[]
  past=0
  gerund=0
  splitted_text=text.split()
  for i in splitted_text:
    i=i.strip(string.punctuation+string.digits)
    if len(i)>2 and i[-2:]=="ed" and i not in exclusions:
      ed_words_list.append(i)
      past+=1
    elif len(i)>3 and i[-3:]=="ing" and i not in exclusions:
      ing_words_list.append(i)
      gerund+=1
  print(f"The words that end with \"ed\" are: \"{', '.join(ed_words_list)}\", and The words that end with \"ing\" are: \"{', '.join(ing_words_list)}\".\nThe total count of the words that end with \"ed\" and \"ing\" is: ")
  return past,gerund
contraction={
    "don't": "do not",
    "can't": "cannot",
    "won't": "will not",
    "it's": "it is",
    "you're": "you are",
    "they're": "they are",
    "we're": "we are",
    "he's": "he is",
    "she's": "she is",
    "i'm": "i am",
    "isn't": "is not",
    "aren't": "are not",
    "wasn't": "was not",
    "weren't": "were not",
    "haven't": "have not",
    "hasn't": "has not",
    "hadn't": "had not",
    "wouldn't": "would not",
    "shouldn't": "should not",
    "couldn't": "could not",
    "doesn't": "does not",
    "didn't": "did not",
    "let's": "let us",
    "that's": "that is",
    "what's": "what is",
    "where's": "where is",
    "who's": "who is",
    "why's": "why is",
    "how's": "how is",
    "there's": "there is",
    "here's": "here is",
    "I've": "I have",
    "you've": "you have",
    "we've": "we have",
    "they've": "they have",
    "that'll": "that will",
    "there'll": "there will",
    "who'll": "who will",
    "I'll": "I will",
    "you'll": "you will",
    "he'll": "he will",
    "she'll": "she will",
    "we'll": "we will",
    "they'll": "they will",
    "would've": "would have",
    "could've": "could have",
    "should've": "should have",
    "must've": "must have",
    "might've": "might have",
    "musn't": "must not",
    "I'd": "I would",
    "you'd": "you would",
    "he'd": "he would",
    "she'd": "she would",
    "it'd": "it would",
    "we'd": "we would",
    "they'd": "they would",
    "gonna": "going to",
    "wanna": "want to",
    "gotta": "got to",
    "gotcha": "got you"
}
def uncontract_word(text):
  """It expands contracted words in the given text to their full forms. This function takes a single parameter: the text to analyze. It returns a new string with all contracted words expanded. The function uses a predefined dictionary of common contractions and their expansions."""
  splitted_text=text.split()
  uncontracted_list=[]
  for i in splitted_text:
    i=i.strip(string.punctuation)
    if i.lower() in contraction.keys():
      uncontracted_list.append(contraction[i.lower()])
    else:
      uncontracted_list.append(i)
  return " ".join(uncontracted_list)
def english_stop_words_removal(text):
  """It removes common English stop words from the given text. This function takes a single parameter: the text to analyze. It returns a new string with all stop words removed. The function uses a predefined list of common English stop words."""
  stop_words_list=["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now", "d", "ll", "m", "o", "re", "ve", "y", "ain", "aren", "couldn", "didn", "doesn", "hadn", "hasn", "haven", "t", "isn", "ma", "mightn", "mustn", "needn", "shan", "shouldn", "wasn", "weren", "won", "wouldn"]
  splitted_text=text.split()
  filtered_text=[]
  for i in splitted_text:
    i=i.strip(string.punctuation+string.digits)
    if i.lower() not in stop_words_list:
      filtered_text.append(i)
  return " ".join(filtered_text)
def title_format(text):
  """It formats the given title according to English title capitalization rules. This function takes a single parameter: the title to format. It returns a new string with the title formatted according to title capitalization rules. The function capitalizes the first and last words of the text, as well as all words that are not common exceptions. Common exceptions include articles, conjunctions, and prepositions."""
  exceptions=["a", "an", "and", "but", "for", "nor", "or", "so", "the", "to", "in", "on", "at", "by", "with", "as", "from", "of", "up", "down", "about"]
  splitted_text=text.split()
  result=[]
  for i in range(len(splitted_text)):
    word=splitted_text[i]
    if i==0 or i==len(splitted_text)-1 or word.lower() not in exceptions:
      result.append(word.capitalize())
    else:
      result.append(word.lower())
  return " ".join(result)
def definite_english_detection(text):
  """It detects and counts definite nouns in the given English text. This function uses a regular expression to find words that are preceded by the definite article 'the'. It returns a formatted string containing the list of definite nouns found and their count."""
  pattern=r'\bthe\s+\w+\b'
  definite_words_list=re.findall(pattern, text, re.IGNORECASE)
  return f"The definite nouns found in the given text are: \"{', '.join(definite_words_list)}\", and their count within the text are: {len(definite_words_list)}"
def indefinite_english_detection(text):
  """It detects and counts indefinite nouns in the given English text. This function uses a regular expression to find words that are preceded by the indefinite articles 'a' or 'an'. It returns a formatted string containing the list of indefinite nouns found and their count."""
  indefinite_pattern=r'\b(a|an)\s+(\w+)\b'
  indefinite_words_list=re.findall(indefinite_pattern, text, re.IGNORECASE)
  collected_list=[" ".join(i) for i in indefinite_words_list]
  return f"The indefinite nouns found in the given text are: \"{', '.join(collected_list)}\", and their count within the text is: {len(collected_list)}"
def sentence_capitalize(text):
  """It capitalizes the first letter of each sentence in a string and removes extra spaces. This function splits the input text into sentences based on the delimiters '?!.' and capitalizes the first letter of each sentence. It joins them back into a single string. This function takes only one parameter which is the string to be processed. It returns the processed string with capitalized sentences and no extra spaces before punctuations, but it returns an empty string if the input text is empty or contains only whitespace."""
  sentences=re.split(r'([.!?])', text)
  capitalized=[]
  for i in sentences:
    if i.strip():
      capitalized.append(i.strip(" ").capitalize())
  return re.sub(r'\s([.!?])', r'\1', " ".join(capitalized))
