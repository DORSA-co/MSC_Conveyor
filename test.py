style_text = """QTextEdit
            {{
                color: rgb(20, 20, 20);
                border: None;
                border-bottom: 2px solid rgba({0}, {1}, {2}, 255);
                background-color: rgba({0}, {1}, {2}, 50);
                padding-left: 55px;
                padding-top: 6px;
                padding-bottom: 3x;
                background-image: url({3});
                background-position: left center;
                background-repeat: no-repeat;
                min-height: 55px;
                max-height: 55px;
            }}

            QTextEdit:disabled
            {{
                color: rgb(20, 20, 20)
            }}"""

# Example usage
red = 255
green = 0
blue = 0
imageUrl = "path/to/image.png"

single_line_style_text = style_text.replace('\n', ' ').replace('\t', ' ')
formatted_style_text = single_line_style_text.format(red, green, blue, imageUrl)

print(formatted_style_text)
