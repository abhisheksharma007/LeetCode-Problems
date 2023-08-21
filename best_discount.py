
offers = {
    'nike' : {
        'min_purchase' : 5000,
        'discount' : 5,
        'combined_offer' : 'puma',
        'combined_disc' : 5,
        'combined_min_purc' : 5000
        },
    'puma' : {
        'min_purchase' : 1000,
        'discount' : 5,
        'combined_offer' : 'nike',
        'combined_disc' : 5,
        'combined_min_purc' : 5000
        },
    'reebok' : {
        'min_purchase' : 3000,
        'discount' : 10
        }
    }

order_details = {
    'nike' :  6000,
    'puma' : 1000,
    'reebok' : 2500,
}

discount = 0
discounted_amt = 0
total_disc_amt = 0
prod_disc_amt = 0
combined_check = {}

for k in offers:
    prod_disc_amt = 0
    if k in order_details:
        if order_details[k] >= offers[k]['min_purchase']:
            if k not in combined_check:
                prod_disc_amt = ((offers[k]['discount']/100) * order_details[k])
        
        if offers[k].get('combined_offer') and offers[k].get('combined_offer') in order_details and offers[k]['combined_offer'] not in combined_check and (order_details[k] + order_details[offers[k]['combined_offer']]) >= offers[k]['combined_min_purc']:
                combined_disc = offers[k]['combined_disc']
                combined_disc_amt = ((combined_disc/100) * (order_details[k] + order_details[offers[k]['combined_offer']]))
                if combined_disc_amt > prod_disc_amt:
                    prod_disc_amt = combined_disc_amt
                    combined_check[offers[k].get('combined_offer')] = combined_check[k] = combined_disc_amt
                
        total_disc_amt += prod_disc_amt
            
print(total_disc_amt)