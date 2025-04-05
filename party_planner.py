#!/usr/bin/env python3

import cgi
import html
party_items = {
    0: ("Cake", 20),
    1: ("Balloons", 21),
    2: ("Music System", 10),
    3: ("Lights", 5),
    4: ("Catering Service", 8),
    5: ("DJ", 3),
    6: ("Photo Booth", 15),
    7: ("Tables", 7),
    8: ("Chairs", 12),
    9: ("Drinks", 6),
    10: ("Party Hats", 9),
    11: ("Streamers", 18),
    12: ("Invitation Cards", 4),
    13: ("Party Games", 2),
    14: ("Cleaning Service", 11)
}

print("Content-type: text/html\n")

form = cgi.FieldStorage()

try:
    raw_indices = form.getvalue("items")

    if not raw_indices:
        raise ValueError("No items were selected.")

    indices = [int(i.strip()) for i in raw_indices.split(",")]

    selected_items = []
    values = []

    for idx in indices:
        if idx in party_items:
            item_name, item_value = party_items[idx]
            selected_items.append(item_name)
            values.append(item_value)
        else:
            raise IndexError(f"Invalid index: {idx}")

    base_code = values[0]
    for val in values[1:]:
        base_code &= val

    original_base_code = base_code

    if base_code == 0:
        base_code += 5
        message = "Epic Party Incoming!"
    elif base_code > 5:
        base_code -= 2
        message = "Let's keep it classy!"
    else:
        message = "Chill vibes only!"

    print("<html><body>")
    print("<h2>Selected Party Items:</h2>")
    print("<ul>")
    for item in selected_items:
        print(f"<li>{html.escape(item)}</li>")
    print("</ul>")
    print(f"<p><strong>Base Party Code:</strong> {original_base_code}</p>")
    print(f"<p><strong>Final Party Code:</strong> {base_code}</p>")
    print(f"<p><strong>Message:</strong> {html.escape(message)}</p>")
    print("</body></html>")

except Exception as e:
    print("<html><body><h2>Error processing form:</h2>")
    print(f"<p>{html.escape(str(e))}</p></body></html>")

