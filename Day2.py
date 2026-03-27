# Day 2: User Input and If-Else Logic
stock_ticker = "TATASTEEL"
buy_price = 140.0

# We use float() because stock prices have decimals
current_price = float(input("Enter the current market price for TATASTEEL: "))

print("--- Portfolio Analysis ---")
if current_price >= buy_price + 10:
    print("Status: Strong profit. Consider securing gains.")
elif current_price > buy_price:
    print("\033[92mStatus: In the green. Hold for long-term.\033[0m")
elif current_price == buy_price:
    print("Status: Breaking even.")
else:
    print("\033[91mStatus: In the red. Analyze market trends before averaging down.\033[0m")