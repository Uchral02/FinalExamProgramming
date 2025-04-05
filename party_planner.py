import cgi # type: ignore

party_items = [
    ("Cake", 20), ("Balloons", 21), ("Music System", 10), ("Lights", 5),
    ("Catering Service", 8), ("DJ", 3), ("Photo Booth", 15), ("Tables", 7),
    ("Chairs", 12), ("Drinks", 6), ("Party Hats", 9), ("Streamers", 18),
    ("Invitation Cards", 4), ("Party Games", 2), ("Cleaning Service", 11)
]

form = cgi.FieldStorage()
selected_indices = form.getlist("items")

selected_items = []
values = []

try:
    for idx in selected_indices:
        index = int(idx)
        item, value = party_items[index]
        selected_items.append(item)
        values.append(value)

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

    print("Content-type: text/html\n")
    print("<html><head><title>Party Planner Result</title></head><body>")
    print("<h2>🎉 Digital Party Planner Results 🎉</h2>")
    print("<p><strong>Selected Items:</strong> " + ", ".join(selected_items) + "</p>")
    print("<p><strong>Base Party Code:</strong> {} (from values: {})</p>".format(original_base_code, " & ".join(map(str, values))))
    print("<p><strong>Final Party Code:</strong> {}</p>".format(base_code))
    print("<p><strong>Message:</strong> {}</p>".format(message))
    print("</body></html>")

except Exception as e:
    print("Content-type: text/html\n")
    print("<html><body><h2>Error processing form:</h2><p>{}</p></body></html>".format(e))
