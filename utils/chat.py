import os
import openai
import MetaTrader5 as mt5
from dotenv import load_dotenv

# Initialize MetaTrader5
mt5.initialize()

# Load the .env file
load_dotenv()

# Now you can access the API key
openai_api_key = os.getenv('OPENAI_API_KEY')

# Set the OpenAI API key
openai.api_key = openai_api_key

# Function to close a position given its ticket
def close_position(ticket):
    # Get the position details
    position = mt5.positions_get(ticket=ticket)
    if position is None:
        print(f"Bot: No position found with ticket {ticket}")
        return

    symbol = position.symbol
    volume = position.volume
    position_type = position.type
    profit = position.profit

    print(f"Bot: Closing position {ticket}")
    print(f"Symbol: {symbol}")
    print(f"Volume: {volume}")
    print(f"Profit: {profit}")

    # Close the position
    trade_request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": volume,
        "type": mt5.ORDER_TYPE_SELL if position_type == mt5.ORDER_TYPE_BUY else mt5.ORDER_TYPE_BUY,
        "position": ticket,
        "magic": 234000,
        "deviation": 20,
        "comment": "Close position",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }
    result = mt5.order_send(trade_request)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print("Failed to close position with ticket #{}".format(ticket))
    else:
        print("Position with ticket #{} closed successfully".format(ticket))

# Function to close positions by symbol and type
def close_positions_by_symbol_and_type(symbol, position_type):
    # Get all positions
    positions = mt5.positions_get()
    
    print(f"Total positions: {len(positions)}")
    
    # Filter positions by symbol and type
    positions_to_close = [position for position in positions if position.symbol == symbol and position.type == position_type]
    
    print(f"Positions to close: {len(positions_to_close)}")
    
    # Close each position
    for position in positions_to_close:
        close_position(position.ticket)

# Main loop to get user input and handle commands
while True:
    # Get user input
    prompt = input("You: ")

    # Generate a response using OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that interfaces with MetaTrader5. You can get open positions, total positions, close a position, close all longs for a symbol, and close all shorts for a symbol."},
            {"role": "user", "content": prompt}
        ]
    )

    # Extract the message from the response
    message = response['choices'][0]['message']['content'].strip()

    # Handle different commands
    if "open positions" in message:
        # Handle "open positions" command
        positions = mt5.positions_get()
        if positions:
            for position in positions:
                print(f"Bot: Position {position.ticket}")
                print(f"Symbol: {position.symbol}")
                print(f"Volume: {position.volume}")
                print(f"Open price: {position.price_open}")
                print(f"Current price: {position.price_current}")
                print(f"Profit: {position.profit}")
                print("------------------------")
        else:
            print("Bot: No open positions.")
    elif message.startswith("close position "):
        # Handle "close position {position_number}" command
        ticket = int(message.split(" ")[2])
        close_position(ticket)
    elif message.startswith("close all ") and " long positions" in message:
        # Handle "close all {symbol} long positions" command
        symbol = message.split(" ")[2]
        close_positions_by_symbol_and_type(symbol, mt5.POSITION_TYPE_BUY)
    elif message.startswith("close all ") and " short positions" in message:
        # Handle "close all {symbol} short positions" command
        symbol = message.split(" ")[2]
        close_positions_by_symbol_and_type(symbol, mt5.POSITION_TYPE_SELL)
    else:
        print("Bot: ", message)