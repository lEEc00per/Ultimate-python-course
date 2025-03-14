name1 = input("Enter your name: ")
name2 = input("Enter Date: ")

letter = '''Dear <|Name|>, 
        You are selected!
        <|Date|>'''
print(letter. replace("<|Name|>", name1).replace("<|Date|>", name2))