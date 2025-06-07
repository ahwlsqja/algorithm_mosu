ss = input()

a_lit = ss.split(" ")

cleaned_list = [item for item in a_lit if item.strip() != ""]

print(len(cleaned_list))