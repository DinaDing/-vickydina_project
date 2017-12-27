with open("html_text.txt", "r") as f:
	text = f.read()


start_position_number = text.find('class="album"')

start_position_number = text.find("<b>", start_position_number)
start_position_number += 3

end_position_number = text.find("</b>", start_position_number)

album = text[start_position_number: end_position_number]

start_position_number = text.find ('_blank">', end_position_number)
start_position_number += 4
end_position_number = text.find('</a', start_position_number)
song = text[start_position_number: end_position_number]
print(song)
print(album)