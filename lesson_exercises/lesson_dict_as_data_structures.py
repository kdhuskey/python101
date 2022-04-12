def contact_card(dictionary):
    print(f'{dictionary["name"]} ({dictionary["email"]})')


customer = {
    'order_status': 'submitted',
    'order_paid': False,
    'order_received': True,
    'name': 'john',
    'email': 'john@gmail.com',
    'company': 'netflix'

}
# contact_card(customer)
customers = [
    { 'name' : 'kyle', 'email': 'kafda@asdf.com', 'company': 'amazon' }, 
    { 'name' : 'james', 'email': 'james@yahoo.com', 'company': 'costco'},
    {'name' : 'brooks', 'email': 'bks@gmail.com', 'company': 'none'}
    
    ]
# contact_card(customers)
for cust in customers:
    contact_card(cust)