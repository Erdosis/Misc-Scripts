<!-- ABOUT THE PROJECT -->
## About The Project

Two small python scripts to help me rip youtube subs from an old google account, and transfer them to a new one.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

1. Navigate to Youtube.com.
2. Locate "Show X More" under your subscriptions and click it.
3. Open Developer Tools by pressing F12.
4. Activate the inspect element feature, then hover over the subscriptions box until it's fully highlighted. Click to select it.
5. In the Developer Tools pane, right-click the highlighted HTML segment and choose Copy > Copy Element.
6. Paste into ytsubrip.html in this folder.



### Usage

From the CLI: 

1. Run `python extractytchannels.py` to create a `channel_list.txt` with all your subscriptions.
2. Run `python sub.py` to open all of the channels in your default browser. They will open in batches of 10. To procede to the next batch, hit enter on the terminal. 



<!-- LICENSE -->
## License

Distributed under the GPL License. See `LICENSE.txt` for more information.
