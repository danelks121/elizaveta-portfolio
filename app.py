from flask import Flask, render_template, abort

app = Flask(__name__)

stylist = {
    "name": "Elizaveta Filippenko",
    "label": "DIGITAL FASHION PORTFOLIO",
    "title": "Fashion Stylist & Creative Director",
    "intro": "Selected styling portfolio and editorial projects.",
    "bio": "Creating visual stories through styling, editorial direction, and fashion imagery.",
    "instagram": "@yourinstagram",
    "email": "your@email.com",
    "phone": "+00 000 000 0000",
    "about_text": "Elizaveta Filippenko is a fashion stylist and creative director working across editorial storytelling, concept-driven styling, and fashion image-making. This trial About page is ready for final text, contact details, and photo updates tomorrow."
}

stories = [
    {'slug': 'blooming-authority', 'title': 'Blooming Authority', 'folder': 'blooming-authority', 'issue': 'EDITORIAL PHOTOSHOOT', 'role': 'Wardrobe Stylist, Creative Director', 'description': 'Editorial project.', 'cover': 'cover.jpg', 'images': ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg']},
    {'slug': 'power-palette', 'title': 'Power Palette', 'folder': 'power-palette', 'issue': 'ISSUE 14', 'kicker': 'EDITORIAL PHOTOSHOOT', 'role': 'Creative Director, Wardrobe Stylist', 'description': 'MOEVIR Magazine issue #11 June 2026', 'cover': 'cover.jpg', 'images': ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg', '10.jpg']},
    {'slug': 'une-etude-en-fleurs', 'title': 'Une Étude En Fleurs', 'folder': 'une-étude-en-fleurs', 'issue': 'EDITORIAL PHOTOSHOOT', 'role': 'Wardrobe Stylist, Creative Direction', 'description': 'Editorial project.', 'cover': 'cover.jpg', 'images': ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg']},
    {'slug': 'private-styling', 'title': 'Private Styling', 'folder': 'private-styling', 'issue': 'ISSUE 10', 'kicker': 'EDITORIAL PHOTOSHOOT', 'role': 'Wardrobe Stylist', 'description': 'GMARO Magazine #11 issue April 2026', 'cover': 'cover.jpg', 'images': ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']},
    {'slug': 'whispers-of-the-fallen', 'title': 'Whispers Of The Fallen', 'folder': 'whispers-of-the-fallen', 'issue': 'ISSUE 09', 'kicker': 'EDITORIAL PHOTOSHOOT', 'role': 'Wardrobe Stylist', 'description': 'VICTOR Magazine Dubai issue #34', 'cover': 'cover.jpg', 'images': ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg']},
    {'slug': 'untethered', 'title': 'Untethered', 'folder': 'untethered', 'issue': 'ISSUE 15', 'kicker': 'EDITORIAL PHOTOSHOOT', 'role': 'Wardrobe Stylist', 'description': 'STYLÉCRUZE Magazine June 2026 issue Vol. 204', 'cover': 'cover.jpg', 'images': ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']},
    {'slug': 'luxury-on-the-rocks', 'title': 'Luxury On The Rocks', 'folder': 'luxury-on-the-rocks', 'issue': 'ISSUE 07', 'kicker': 'EDITORIAL PHOTOSHOOT', 'role': 'Creative Director, Wardrobe Stylist', 'description': 'VOUS Magazine to be published soon', 'cover': 'cover.jpg', 'images': ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg', '10.jpg']},
    {'slug': 'she-is-power', 'title': 'She Is Power', 'folder': 'she-is-power', 'issue': 'ISSUE 13', 'kicker': 'EDITORIAL PHOTOSHOOT', 'role': 'Wardrobe Stylist', 'description': 'MOEVIR Magazine issue #19 April 2026', 'cover': 'cover.jpg', 'images': ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg']},
    {'slug': 'velvet-society', 'title': 'Velvet Society', 'folder': 'velvet-society', 'issue': 'ISSUE 08', 'kicker': 'EDITORIAL PHOTOSHOOT', 'role': 'Creative Director, Wardrobe Stylist', 'description': 'MALVIE Magazine June 2026 issue', 'cover': 'cover.jpg', 'images': ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg']},
    {'slug': 'fecc-march', 'title': 'Fecc March', 'folder': 'fecc-march', 'issue': 'ISSUE 05', 'kicker': 'EDITORIAL PHOTOSHOOT', 'role': 'Fashion Assistant', 'description': 'FECC Magazine March 2026 issue', 'cover': 'cover.jpg', 'images': ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg', '10.jpg', '11.jpg']},
    {'slug': 'iconic', 'title': 'Iconic', 'folder': 'iconic', 'issue': 'ISSUE 11', 'kicker': 'EDITORIAL PHOTOSHOOT', 'role': 'Creative Director, Wardrobe Stylist', 'description': 'QUADRO Magazine', 'cover': 'cover.jpg', 'images': ['1.jpg', '2.jpg', '3.jpg', '4.jpg']},
    {'slug': 'porcelain-hour', 'title': 'Porcelain Hour', 'folder': 'porcelain-hour', 'issue': 'ISSUE 12', 'kicker': 'EDITORIAL PHOTOSHOOT', 'role': 'Wardrobe Stylist', 'description': 'VOUS Magazine to be published soon', 'cover': 'cover.jpg', 'images': ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']},
    {'slug': 'new-skin', 'title': 'New Skin', 'folder': 'new-skin', 'issue': 'ISSUE 03', 'kicker': 'EDITORIAL PHOTOSHOOT', 'role': 'Wardrobe Stylist', 'description': 'HIGH VOLT Magazine issue #288 April 2026', 'cover': 'cover.jpg', 'images': ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg']},
    {'slug': 'quiet-flame', 'title': 'Quiet Flame', 'folder': 'quiet-flame', 'issue': 'ISSUE 01', 'kicker': 'EDITORIAL PHOTOSHOOT', 'role': 'Wardrobe Stylist', 'description': 'VANGUARD Magazine #44 Vol. 14 January 2026', 'cover': 'cover.jpg', 'images': ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg']},
    {'slug': 'no-more-hiding', 'title': 'No More Hiding', 'folder': 'no-more-hiding', 'issue': 'ISSUE 02', 'kicker': 'EDITORIAL PHOTOSHOOT', 'role': 'Wardrobe Stylist', 'description': 'BLISS Magazine issue Vol. 5 March 2025', 'cover': 'cover.jpg', 'images': ['1.jpg', '2.jpg', '3.jpg', '4.jpg']},
    {'slug': 'rising-within', 'title': 'Rising Within', 'folder': 'rising-within', 'issue': 'ISSUE 04', 'kicker': 'EDITORIAL PHOTOSHOOT', 'role': 'Wardrobe Stylist', 'description': 'BEAUTICA Magazine issue #2 March 2026', 'cover': 'cover.jpg', 'images': ['1.jpg', '2.jpg', '3.jpg', '4.jpg']}
]

story_lookup = {story["slug"]: story for story in stories}


@app.route("/")
def home():
    return render_template("index.html", stylist=stylist, stories=stories)


@app.route("/story/<slug>")
def story(slug: str):
    selected_story = story_lookup.get(slug)
    if not selected_story:
        abort(404)
    return render_template("story.html", stylist=stylist, story=selected_story)


@app.route("/about")
def about():
    return render_template("about.html", stylist=stylist)


if __name__ == "__main__":
    app.run(debug=False)