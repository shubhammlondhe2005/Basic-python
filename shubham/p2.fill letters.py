#write a program to fill in a letter template given below with name and date.

letter='''Dear <|Name|>,
You are selected!
<|Date|>'''

print(letter.replace("<|Name|>","shubham").replace("<|Date|>","18th march")) 
#replace i used for the replacig the name and the date in the code