def should_serve_customer(customer_age, on_break, time):
    return customer_age >= 21 and on_break != True and time >= 5 and time <= 10
        
