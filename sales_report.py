# original code

"""Generate sales report showing total melons each salesperson sold."""

salespeople = []
melons_sold = []

# make a file object "f" from the sales report file
f = open('sales-report.txt')
# iterate over each line in the file (each order)
for line in f:
    # get rid of extra whitespace/new lines, etc.
    line = line.rstrip()
    # split up the line by '|' character and put each element in a list called entries
    entries = line.split('|')
    # grab the first of the entries, this is the salesperson
    salesperson = entries[0]
    # grab the last of the entries, this is the number of melons sold. cast as int
    melons = int(entries[2])

    # if this salesperson is already in our list
    if salesperson in salespeople:
        position = salespeople.index(salesperson)
        #add the melons in this order to the total number of melons sold for that sales person
        # the lists are linked by having the same index
        melons_sold[position] += melons
    # otherwise add the salesperson to the list
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)

# print the number of melons sold by each sales person
for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')

print('--------------------------------------------')
# improved code: use a dictionary instead of two lists. use .get() to replace need for conditional
"""Generate sales report showing total melons each salesperson sold."""

def get_sales_info(filename):
    """ Takes in a filename and returns a dictionary with salespeople as keys and melons sold as values
    File is a text file with each line being a order with salesperson, amount paid, and melons sold separated by | """
    # dictionary where salesperson will be key, melons sold will be value
    melon_sales = {}

    # make a file object "f" from the sales report file
    with open(filename) as f:
    # iterate over each line in the file (each order)
        for line in f:
            # get rid of extra whitespace/new lines, etc.
            line = line.rstrip()
            # split up the line by '|' character
            salesperson, payment, melons = line.split('|')

            melon_sales[salesperson] = melon_sales.get(salesperson, 0) + int(melons)

    return melon_sales

def print_sales_report(melon_sales):
    """ Takes in a dictionary with {salesperson:total melons sold} and prints out sales report. """
# print the number of melons sold by each sales person
    for salesperson, melons in melon_sales.items():
        print(f'{salesperson} sold {melons} melons')

melon_sales = get_sales_info('sales-report.txt')
print_sales_report(melon_sales)


