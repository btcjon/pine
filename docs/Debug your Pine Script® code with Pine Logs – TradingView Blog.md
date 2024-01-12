(https://www.tradingview.com/)
(/blog/)
PINE SCRIPT®(HTTPS://WWW.TRADINGVIEW.COM/BLOG/EN/CATEGORY/PINE/)

## Debug Your Pine Script® Code With Pine Logs

Aug 29, 2023
Take your Pine Script® debugging to another level with our new log.*() functions, which display text in the new Pine Logs pane as the script executes. The three new logging functions are:
log.error() (https://www.tradingview.com/pine-scriptreference/v5/#fun_log.error) creates messages of type "Error" displayed in red. log.info() (https://www.tradingview.com/pine-scriptreference/v5/#fun_log.info) creates messages of type "Info" displayed in gray. log.warning() (https://www.tradingview.com/pine-scriptreference/v5/#fun_log.warning) creates messages of type "Warning" displayed in orange.

You can view Pine Logs by selecting "Pine Logs…" from the Editor's "More" menu, or from the "More" menu of a script loaded on your chart if it uses log.*() functions.

Pine Logs work everywhere: on historical bars, in real time, and in Replay mode. The logging functions can be called from any type of script (indicator, strategy or library) and from anywhere in the script, including local blocks, loops and from inside request.security() (https://www.tradingview.com/pine-scriptreference/v5/#fun_request.security) and similar functions. You can call logging functions in two ways: using only a string argument, or using a formatting string and a list of values in str.format()
(https://www.tradingview.com/pine-script-reference/v5/#fun_str.format) fashion. Scripts using logs must be personal scripts; privately or publicly published scripts cannot generate logs, even if they contain calls to log.*() functions. The following code example uses all three logging functions:

//@version=5 indicator("Pine Logs") if barstate.ishistory if bar_index % 100 == 0 log.warning("\nBar index: {0,number,#}", bar_index) else // Realtime bar processing. varip lastTime = timenow
    varip updateNo = 0
    if barstate.isnew updateNo := 0 log.error("\nNew bar") else log.info("\nUpdate no: {0}\nclose: {1}\nSeconds elapsed: {2}", updateNo, close updateNo += 1 lastTime := timenow plot(timenow)
The example displays the bar index on every hundredth historical bar using an orange warning message. In real time, it displays an error message in red for each new bar, and for each real-time update, it creates an information message in gray showing the update number, the close (https://www.tradingview.com/pine-script-reference/v5/#var_close) price, and the time elapsed since the last chart update. To see Pine Logs in action:
-. Save the above code example to a personal script and add it to a chart with an active market. /. Open the "Pine Logs" pane using the Editor's "More" menu or the indicator's "More" menu on the chart.

A timestamp prefixes each log entry. It is the bar's opening time (https://www.tradingview.com/pine-script-reference/v5/#fun_time) for historical bars, and the current time for real-time messages. Newer messages appear at the bottom of the pane. Only the last 10,000 messages will be displayed for historical bars; real-time messages are appended to those. The top of the pane contains icons allowing you to start/stop the logging, specify a starting date, filter the logs by message type, and search the logs. The search field contains a sub-menu allowing you to match cases, whole words, and use regex. When you hover over a log message, icons appear that allow you to view the source code that has generated the message or jump to the corresponding chart bar:
When multiple scripts on your chart use logs, each one maintains its own set of messages. You can switch between each script's logs by using the dropdown at the top of the Pine Logs pane:
To stay up to date on new Pine Script® features, keep an eye on the User Manual's Release notes (https://www.tradingview.com/pine-scriptdocs/en/v5/Release_notes.html). The PineCoders (https://www.tradingview.com/u/PineCoders/) account also broadcasts updates from its Squawk Box (https://t.me/PineCodersSquawkBox) on Telegram, its Twitter account (https://twitter.com/PineCoders), and from the Pine Script® Q&A (https://www.tradingview.com/chat/#BfmVowG1TZkKO235) public chat on TradingView.

We hope you find this highly-requested feature as useful as we think it'll be, and please do keep sending us your feedback and suggestions (https://www.reddit.com/r/TradingView/) so we can make the platform the best it can be. We build TradingView for you, and we're always keen to hear your thoughts.

- Team TradingView

## Look Ȅrst  Then Leap

TradingView is built for you, so make sure you're getting the most of our awesome features
(https://www.tradingview.com/chart/?

Launch Chart symbol=NASDAQïAAPL)
(https://twitter.com/tradingview/)
(https://www.facebook.com/tradingview/)
(https://www.youtube.com/channel/UCfOflihrkOKDQZ_ZKtF2VfQ/)
(https://www.instagram.com/tradingview/)
(https://t.me/tradingview/)
(https://www.tiktok.com/@tradingview
(https://www.reddit.com/r/Tradin
(https://www.linkedin.com/com

| Products                                | Company        |
|-----------------------------------------|----------------|
| Chart                                   |                |
| (https://www.tradingview.com/chart/)    |                |
| About                                   |                |
| (https://www.tradingview.com/contacts/) |                |
| Widgets                                 |                |
| (https://www.tradingview.com/           |                |
| Refer a friend                          |                |
| (https://www.tradingview.com/share-     |                |
| your-love/?                             |                |
| source=footer&feature=refer_friend)     |                |
| How It Works                            |                |
| (https://www.tradingview.com/how-       |                |
| it-works/)                              |                |
| Advertising                             |                |
| (https://www.tradingview.com/           |                |
| info/)                                  |                |
| Pine Script                             |                |
| (https://www.tradingview.com/pine-      |                |
| script-                                 |                |
| docs/en/v4/Introduction.html)           |                |
| Ideas                                   |                |
| (https://www.tradingview.com/ideas/)    |                |
| Features                                |                |
| (https://www.tradingview.com/features/) | Stock Screener |
| (https://www.tradingview.com/screener/) |                |
| Scripts                                 |                |
| (https://www.tradingview.com/scripts/)  |                |
| Website & Broker                        |                |
| Solutions                               |                |
| (https://www.tradingview.com/           |                |
| for-the-web/)                           |                |
| Pricing                                 |                |
| (https://www.tradingview.com/gopro/)    | Streams        |
| (https://www.tradingview.com/streams/)  |                |
| Forex Screener                          |                |
| (https://www.tradingview.com/forex-     |                |
| screener/)                              |                |
| Wall of Love                            |                |
| (https://www.tradingview.com/wall-      |                |
| of-love/)                               |                |
| House rules                             |                |
| (https://www.tradingview.com/house-     |                |
| Charting solutions                      |                |
| (https://www.tradingview.com/           |                |
| stock-forex-bitcoin-                    |                |
| charting-library/)                      |                |
| rules/)                                                   | Blog                  |
|-----------------------------------------------------------|-----------------------|
| (https://www.tradingview.com/blog/en/)                    |                       |
| Crypto Screener                                           |                       |
| (https://www.tradingview.com/crypto-                      |                       |
| screener/)                                                |                       |
| Moderators                                                |                       |
| (https://www.tradingview.com/moderators/)                 |                       |
| Lightweight Charting                                      |                       |
| Library                                                   |                       |
| (https://www.tradingview.com/                             |                       |
| charts/)                                                  |                       |
| Security vulnerability                                    |                       |
| (https://www.tradingview.com/bounty/)                     | Economic Calendar     |
| (https://www.tradingview.com/markets/currencies/economic- |                       |
| calendar/)                                                |                       |
| Status page                                               |                       |
| (https://status.tradingview.com/)                         |                       |
| Pine Wizards                                              |                       |
| (https://www.tradingview.com/pine-                        |                       |
| wizards/)                                                 |                       |
| Brokerage Integration                                     |                       |
| (https://www.tradingview.com/                             |                       |
| integration/)                                             |                       |
| Terms of Use                                              |                       |
| (https://www.tradingview.com/policies/)                   |                       |
| Chat                                                      |                       |
| (https://www.tradingview.com/chat/)                       |                       |
| Earnings Calendar                                         |                       |
| (https://www.tradingview.com/markets/stocks-              |                       |
| usa/earnings/)                                            |                       |
| Partner program                                           |                       |
| (https://www.tradingview.com/                             |                       |
| program/)                                                 |                       |
| Disclaimer                                                |                       |
| (https://www.tradingview.com/disclaimer/)                 |                       |
| Markets                                                   |                       |
| (https://www.tradingview.com/markets/)                    | Content Streams & RSS |
| (https://www.tradingview.com/                             |                       |
| tools/)                                                   |                       |
| Help Center                                               |                       |
| (https://www.tradingview.com/support/)                    |                       |
| Privacy Policy                                            |                       |
| (https://www.tradingview.com/privacy-                     |                       |
| policy/)                                                  |                       |
| Cookies Policy                                            |                       |
| (https://www.tradingview.com/cookies-                     |                       |
| policy/)                                                  |                       |

(https://www.tradingview.com/desktop/)
DOWNLOAD
Desktop app Select market data provided by ICE Data services (https://www.theice.com/market-data)
© 2023 TradingView