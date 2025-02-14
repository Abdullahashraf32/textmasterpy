How to Use the Framework
After ensuring that the framework is correctly installed on your device, it is time to explore its features and learn how to benefit from its various functions.
The framework consists of 33 functions, categorized into three main groups:
1️⃣- generalprocessing: It contains 19 functions applicable to both English and Arabic texts.
2️⃣- englishprocessing: It contains 9 functions designed specifically for English texts.
3️⃣- arabicprocessing: It contains 5 functions designed specifically for Arabic texts.
IMPORTING AND USING THE FRAMEWORK
You can import the framework using the import statement and call functions from any category as needed.
Example using generalprocessing functions:
import textmasterpy
print(textmasterpy.generalprocessing.character_count("This is a test"))
= Output: "11"
Example using englishprocessing functions:
import textmasterpy
print(textmasterpy.englishprocessing.title_format("the old man and the sea"))
= Output: "The Old Man and the Sea"
= Example using arabicprocessing functions:
import textmasterpy
print(textmasterpy.arabicprocessing.diacritics_removal("هَذَا أَخِي الصَّغِيرُ"))
= Output: "هذا أخي الصغير"
USING ALIASES FOR EASIER ACCESS
To make your code cleaner and more efficient, you can assign an abbreviated name to the framework:
Using an alias for the full framework:
import textmasterpy as tm
print(tm.englishprocessing.title_format("the old man and the sea"))
Importing a specific category directly:
from textmasterpy import generalprocessing
print(generalprocessing.character_count("this is a test"))
Using an alias for a specific category:
from textmasterpy import generalprocessing as gp
print(gp.character_count("this is a test"))
GETTING HELP ON FUNCTIONS
If you need more details about any function, you can use Python's built-in help() function.
Example: Getting help on character_count function:
import textmasterpy
help(textmasterpy.generalprocessing.character_count)
Output:
"It counts the total number of characters in the given text, excluding spaces. 
This function takes a single parameter: the text to analyze. 
It returns the total count of characters in the text. 
The function is useful for determining the length of the text in terms of characters."
Note: 
Ensure you reference the function correctly by including its category (generalprocessing, englishprocessing, or arabicprocessing).
 SUMMARY
= The framework provides 33 functions categorized under three main groups.
= You can import the entire framework or import specific categories for better efficiency.
= Aliases (as tm, as gp, etc.) can make your code more readable.
= The help() function can be used to retrieve detailed documentation for any function.
Now, you're ready to use textmasterpy efficiently! Happy coding!