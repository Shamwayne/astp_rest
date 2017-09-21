import random
import os

string_to_parse = "NUM5-STR10-DATE"

generator = string_to_parse.split("-")
print(generator)

for thingy in generator:
	if 'NUM' in thingy:
		num_of_elements = int(thingy.strip("NUM"))

		""" GENERATE THAT ISH MUNOMU """
	if 'STR' in thingy:
		num_of_elements = int(thingy.strip("STR"))
		""" GENERATE THAT ISH MUNOMU """
	if 'DATE' in thingy:
		num_of_elements = int(thingy.strip("STR"))
		""" GENERATE THAT ISH MUNOMU """