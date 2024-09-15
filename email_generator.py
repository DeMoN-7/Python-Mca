def gen(sapid):
    list_of_emails = [ f"{ id }@stu.upes.ac.in" for id in sapid ]
    return list_of_emails
sapids = [123,234324,345345,4545]
wwe=gen(sapids)
print(wwe)

