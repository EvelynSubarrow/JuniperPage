# Juniper Page
This is a simple library/command line tool to send pages to Spok (perhaps better known by their former name US Mobility) pagers.

## Usage
`./juniper_page.py 0123456789 "Broadsword calling Danny Boy, Broadsword calling Danny Boy"`

## Dependencies
* [requests](https://pypi.org/project/requests/)

## Licence
MIT licence for now (I'm nothing if not consistent)

## Disclaimer
This tool is subject to Spok's Acceptable Use Policy, and to relevant US regional and federal laws regarding telecoms. This project
isn't affiliated with or endorsed by Spok.

## Relevant documentation

Reproduced below is the relevant section of the documentation from Spok's [website](https://www.spok.com/resources/paging-faqs-user-guides/).
See under "Protocols" for more options.


```
HTTP POST to http://www.usamobility.net/cgi-bin/wwwpage.exe

VALUES ARE:

PIN: This is either a 10 or 7 digit number.
MSSG: This is the text part of the message.
Q1: Q1=1 will echo the message; Q1=0 will not.

FOR TWO-WAY CUSTOMERS:

HTTP POST to http://www.usamobility.net/cgi-bin/wwwthoway.exe

REQUIRED VALUES ARE:

GW_PIN: This is either a 10 or 7 digit number or an alias name.
MSSG: This is the text part of the message.

OPTIONAL VALUES:

resp_route: This is a value of “Pager” or “Email” indicating the type of address to route replies or delivery notifications to.
resp_addr: This is the address to send replies and delivery notifications to.

The following Optional Values require resp_route and resp_addr to be defined for the feature to work.
confirm_receipt_str: This must be set to “confirm_page_delivery” if delivery notification is required.
resp_a_string: This is the first custom response choice.
resp_b_string: This is the second custom response choice.
resp_c_string: This is the third custom response choice.
resp_d_string: This is the forth custom response choice.
resp_e_string: This is the fifth custom response choice.
resp_f_string: This is the sixth custom response choice.

The HTTP ‘GET’ Method:

The HTTP ‘Get’ method is disabled. Disabling the GET METHOD on our servers acts as a spam filter for our customers.

Example:
http://www.usamobility.net/cgi-bin/usamobilitypage.exe?ACCESS=1234567890&PIN=1234567890&MSSG=blah
This will not work.

```
