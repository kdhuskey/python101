## Phonebook Dictionary

# phonebook_dict = {
#   'Alice': '703-493-1834',
#   'Bob': '857-384-1234',
#   'Elizabeth': '484-584-2923'
# }
# print(phonebook_dict['Elizabeth'])
# phonebook_dict['Kareem'] = '938-489-1234'
# # print(phonebook_dict)
# bye_alice = phonebook_dict.pop('Alice')
# # print(phonebook_dict)
# print(bye_alice)
# phonebook_dict['Bob'] = '968-345-2345'
# print(phonebook_dict)

# for i in phonebook_dict:
#     print(i)
#     print(phonebook_dict[i])
# for i in phonebook_dict:
    # print(i, phonebook_dict[i])

## Nested Dictionary

# ramit = {
#   'name': 'Ramit',
#   'email': 'ramit@gmail.com',
#   'interests': ['movies', 'tennis'],
#   'friends': [
#     { 'name': 'Jasmine', 'email': 'jasmine@yahoo.com', 'interests': ['photography', 'tennis'] },
#     { 'name': 'Jan', 'email': 'jan@hotmail.com', 'interests': ['movies', 'tv'] }
#   ]
# }
# print(ramit['email'])
# print(ramit['interests'][0])
# print(ramit['friends'][0]['email'])
# print(ramit['friends'][1]['interests'][1])


## Letter Histogram

# user_input = input('Please enter a word: ')
# new_dict = {}
# for i in user_input:
#     if i not in new_dict:
#         new_dict[i] = 0
#     new_dict[i] += 1
# print(new_dict)


## Sentence

user_sentence = input('Please enter a sentence: ').split(" ")
sent_dict = {}


for index in user_sentence:
    if index not in sent_dict:
        sent_dict[index] = 0
    sent_dict[index] += 1
print(sent_dict)