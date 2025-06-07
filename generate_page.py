# generate_page.py

def generate_html_page(things_i_like_list):
    """
    Generates a static HTML file for the '101 Things I Like' list.
    """
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>101 Things I Like</title>
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
        <style>
            body {{
                font-family: 'Poppins', sans-serif;
                margin: 0;
                padding: 40px 20px;
                line-height: 1.8;
                color: #333;
                background-color: #f9f9f9;
                display: flex;
                flex-direction: column;
                align-items: center;
                min-height: 100vh;
            }}
            h1 {{
                color: #5a5a5a;
                text-align: center;
                font-size: 2.8em;
                margin-bottom: 40px;
                letter-spacing: 1px;
                text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
            }}
            .list-container {{
                max-width: 800px;
                width: 100%;
                background-color: #fff;
                padding: 30px 40px;
                border-radius: 12px;
                box-shadow: 0 8px 16px rgba(0,0,0,0.08);
            }}
            ol {{
                list-style-type: decimal;
                padding-left: 28px;
                margin: 0;
            }}
            li {{
                margin-bottom: 12px;
                padding: 10px 15px;
                border-radius: 8px;
                transition: background-color 0.3s ease, transform 0.2s ease, box-shadow 0.2s ease;
                cursor: pointer;
                font-size: 1.1em;
            }}
            li:hover {{
                background-color: #e6f7ff;
                transform: translateX(5px);
                box-shadow: 0 4px 8px rgba(0,0,0,0.06);
            }}
            @media (max-width: 768px) {{
                body {{
                    padding: 20px 10px;
                }}
                h1 {{
                    font-size: 2em;
                    margin-bottom: 30px;
                }}
                .list-container {{
                    padding: 20px 25px;
                }}
                li {{
                    font-size: 1em;
                    padding: 8px 10px;
                }}
            }}
        </style>
    </head>
    <body>

        <h1>101 Things I Like ✨</h1>

        <div class="list-container">
            <ol>
    """

    # Add each item from your Python list into the HTML ordered list
    for item in things_i_like_list:
        html_content += f"                <li>{item}</li>\n"

    html_content += f"""
            </ol>
        </div>

    </body>
    </html>
    """

    # Write the content to an HTML file
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("index.html generated successfully!")

# --- YOUR 101 THINGS GO HERE ---
# Create a Python list with your 101 things
# You can easily edit this list in one place!
my_likes = [
    "Saya suka harumnya bunga-bunga",
    "Saya suka melihat taman maupun pemandangan hijau-hijau ketika butuh refreshing",
    "Saya suka menggambar random kalau sedang nganggur",
    "Saya suka menggunakan emoji/GIF ketika chattingan",
    "Saya suka ketika dapat menyelesaikan lego",
    "Saya senang ketika dapat prepare untuk berpergian/travelling",
    "Saya suka merekam permainan gitar/keyboard saya",
    "Saya suka memakai baju yang nyaman saya pakai",
    "Saya suka ketika dapat tenang setelah panik/cemas",
    "Saya suka ketika dapat menemukan cara baru untuk makan sesuatu",
    "Saya suka jari-jari tangan saya yang panjang sehingga bagus ketika di-nail art",
    "Saya suka membaca quotes-quotes menarik",
    "Saya suka belanja skincare yang sudah cocok sama saya",
    "Saya suka ketika dapat menyelesaikan buku bacaan",
    "Saya senang ketika berhasil memainkan chord gitar yang sulit",
    "Saya suka ketika dapat menyelesaikan buku bacaan",
    
    "The smell of rain after a dry spell",
    "A perfectly cooked steak",
    "Discovering a new, binge-worthy TV series",
    "The sound of waves crashing on the shore",
    "Waking up before my alarm clock",
    "Solving a challenging puzzle",
    "A warm blanket on a cold day",
    "The feeling of fresh, clean laundry",
    "Seeing old friends unexpectedly",
    "The first sip of coffee in the morning",
    # ... and so on, until you have 101 things!
    # Make sure to add commas after each item except the last one.
    "Finishing a satisfying workout"
]

# Ensure you have exactly 101 items (or adjust the title accordingly)
# if len(my_likes) != 101:
#     print(f"Warning: You have {len(my_likes)} items, not 101. Adjust the list or the title!")

# Call the function to generate the HTML page
generate_html_page(my_likes)