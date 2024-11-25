# Blind Auction Project

## Overview
The **Blind Auction Project** is a Python-based program that simulates a secret auction. Participants can anonymously place their bids, and the program determines the highest bidder at the end of the auction.

---

## Features
- Allows multiple participants to place secret bids.
- Stores bid data securely until the program determines the winner.
- Identifies and announces the highest bidder with their bid amount.
- User-friendly interface with prompts for input and clear instructions.

---

## Requirements
This project requires **Python 3.x**. No additional libraries are needed as it uses Python's built-in functionality.

---

## How to Use
1. Clone or download this repository to your local machine.
2. Open the project in your preferred Python IDE or text editor.
3. Run the script in a terminal or IDE.

### Steps to Run the Auction
1. Launch the program.
2. Each participant will:
   - Enter their name.
   - Enter their bid amount in dollars.
3. The program will ask if there are more participants:
   - Type `yes` to allow the next participant to bid.
   - Type `no` to end the auction and display the winner.
4. The program announces the highest bidder and their bid amount.

---

## Example
```
Welcome to the secret auction program!
Write your name: Alice
State your bid value: $300
If there are any other bidders type yes, otherwise type no to exit the program. yes
Write your name: Bob
State your bid value: $450
If there are any other bidders type yes, otherwise type no to exit the program. no
The highest bidder is Bob with a bid of 450 dollars
```

---

## Code Explanation
Below is a brief explanation of the key sections of the code:

### 1. Program Setup
- **`bidder_info`**: A dictionary used to store participants' names as keys and their bid amounts as values.
- **`program_run`**: A boolean variable controlling the program's loop.

### 2. Adding Bids
- The `add_new_info` function takes a name and a bid value as arguments and adds them to the `bidder_info` dictionary.

### 3. Determining the Winner
- After all participants have entered their bids, the program iterates through the dictionary to identify the highest bidder and their bid.

### 4. User Interaction
- The program continuously prompts for input until there are no more bidders.

---

## Contributing
If you'd like to contribute to this project:
1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a Pull Request.

---

## Acknowledgments
- Inspired by the concept of blind auctions to ensure fairness and anonymity.
- Built using Python's simple and effective data structures and input-output methods.

