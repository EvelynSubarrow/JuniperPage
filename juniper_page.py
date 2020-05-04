#!/usr/bin/env python3

# builtin
import argparse

# Third party
import requests

def send_page_usa_mobility(pager_identifier: str, message: str) -> bool:
    """Send a page to a USA mobility (or 'spok', even worse) pager subscriber. Return indicates reported success."""
    if pager_identifier.isnumeric() and len(pager_identifier) not in (7, 10):
        raise ValueError("Numeric identifier provided but this isn't the required length (7 or 10 digits)")

    if len(message) > 240:
        raise ValueError("Message must not exceed 240 characters in length")
    if any([ord(a)&0x80 for a in message]):
        raise ValueError("Message must be within 7-bit ASCII range (00..7F)")

    r = requests.post("http://www.usamobility.net/cgi-bin/wwwpage.exe", data={
        "PIN": pager_identifier,
        "MSSG": message,
        "Q1": "1"
        })
    return """<span CLASS="TEXTBLKBOLD">Page Sent</span>""" in r.text

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("pager_identifier", type=str, help="Subscriber number or identifier")
    parser.add_argument("message", type=str, help="Message, lower half ASCII only")
    args = parser.parse_args()

    pager_identifier, message = args.pager_identifier, args.message


    success = send_page_usa_mobility(pager_identifier, message)
    print("OK"*success or "FAILED")
    exit(success)
