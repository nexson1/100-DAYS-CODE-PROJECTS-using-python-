print('WELCOME TO MY BIDDER APP\n PROCEED TO BID!!')

bids = {}

def bid_calculation(bids):

    highest_bid = 0
    winner = ''
    for bidder in bids:
        if  highest_bid < bids[bidder]:
            highest_bid = bids[bidder]
            winner = bidder
    print(f'the winner is {winner} with a bid of ${highest_bid}')




continuation = True

while continuation:

    user = input('Enter Username: ')
    bid = int(input('Enter bid: $'))
    bids[user] = bid
    user_choice = input('Do you wish to continue? "Yes" or "No"').lower()
    if user_choice =='no':
        continuation = False
        bid_calculation(bids)

    else:
        print('\n' * 1)




