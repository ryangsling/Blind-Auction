print("Welcome to the secret auction program!")
program_run = True
bidder_info = {}
while program_run:
    name = input("Write your name: ")
    bid = int(input("State your bid value: $"))
    def add_new_info(new_name,new_bid):
        bidder_info[new_name] = new_bid
    add_new_info(name,bid)
    option = input("If there are any other bidders type yes, otherwise type no to exit the program. ")
    if option=="no":
        mx = 0
        for key in bidder_info:
            bids = bidder_info[key]
            if bids>mx:
                mx=bids
                keys=key
        print(f"The highest bidder is {keys} with a bid of {mx} dollars")
        program_run = False


