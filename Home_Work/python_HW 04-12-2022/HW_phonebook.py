
phone_book = []
while True:
    user_input = int(input(""" <<< ~ Electronic Phone Book ~ >>>
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Quit
What would you like to do? Please select(1-5) """))

    if user_input == 1:
        person = input('Who are you looking for? ')
        for contact in phone_book:
            if person == contact['Name']:
                i = phone_book.index(contact)
                print(phone_book[i])
    elif user_input == 2:
        new_contact_name = input('Ok, what is the name of the contact you want saved? ')
        new_contact_num = (input('And what is their number? '))
        new_contact = {'Name': new_contact_name, 'Phone Number': new_contact_num}
        phone_book.append(new_contact)
        print(f'Contact info for {new_contact_name} stored.')
    elif user_input == 3:
        deleted_contact = input('Who would you like to no longer speak to? ')
        for contact in phone_book:
            if deleted_contact == contact['Name']:
                i = phone_book.index(contact)
                del phone_book[i]
        print(f'Contact info for {deleted_contact} is now deleted.')
    elif user_input == 4:
        for i in phone_book:
            print(i)
    elif user_input == 5:
        print('Bye for now!')
        break
    else:
        exit