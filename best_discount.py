# Problem Statement
# I am ordering Nike Shoes (6000), Puma T-Shirt (1000) and Reebok Jeans (2500)

# Offers: 
# Puma : 5% discount on purchase of above 1000
# Nike + Puma : 5% discount on purchase of above 5000
# Reebok : 10% discount on purchase of above 3000

# But Puma product should not be considered in both offers.
# As per 1st Offer : 5% for Puma Product
# As per 2nd Offer : 5% for only Nike Product (As alone Nike product is above 5000)

# But if Puma Product would be of 500 and Nike would be of 4500 then in that case 2nd offer would have been applied as it will give more discount

# Both should be applied 1 and 2
# We want to reward max reward to the user



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