
# Final Project - Jame Huang
 
 
 This is my final project for TECH 2335 Summer 2022.


I create a program that informs a budding trader whether there would be an arbitrage opportunity in the global crypto markets, for example, the price of Bitcoin may be $10,000 in one region and $15,000 in another.

Due to the extreme volalitlity of the nascent crypto market, the opportunity will be risk-adjusted based on the traders' risk tolerance (which may be arbitrary).

In attempting to connect via API with overseas crypto centralized exchanges, I learned that all of them required either a premium subscription (not free) or required enhanced verificiation (required me to uploaded a picture of myself and an ID), which I was not willing to do.

To get around this, for demostration purposes, I decided to pick a specific market (South Korea), and downloadeded a csv file listing daily prices of BTC in South Korea from: https://www.investing.com/crypto/bitcoin/btc-krw-historical-data; I then converted the Korean won (KRW) currency back to USD by multiplying each daily close with the daily exchange rate from: https://www.investing.com/crypto/bitcoin/btc-krw-historical-data. (I could not utilize alphavantage's exchange rate because it did not have historical values).


Step 1:
Install Chart Studio with "$pip install chart_studio" via the terminal.

Step 2:
Run the program from a terminal via: $python program.py

Step 3:
Check historical arbitrage opportunities with markets outside of the USA by inputting crypto symbol (for demo purposes, please use BTC). We will be using the USA market as the benchmark.

Step 4:
Input API key for Alphavantage

Step 5: 
Input the market outside of the USA to view historical arbitrage opportunities (for demo purposes, please use KRW for the South Korean Won).




