from flask import Flask, render_template, abort

app = Flask(__name__)

stylist = {
    "name": "Elizaveta Filippenko",
    "intro": "Selected styling portfolio and editorial projects.",
    "bio": "A fashion styling portfolio featuring editorial shoots, visual storytelling, and selected creative works.",
}

stories = [
    {'slug': 'power-palette', 'title': 'Power Palette', 'folder': 'power-palette', 'issue': 'ISSUE 14', 'kicker': 'EDITORIAL PHOTOSHOOT', 'description': 'MOEVIR Magazine issue #11 June 2026', 'cover': 'cover.jpg', 'images': ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg', '10.jpg']},
    {'slug': 'private-styling', 'title': 'Private Styling', 'folder': 'private-styling', 'issue': 'ISSUE 10', 'kicker': 'EDITORIAL PHOTOSHOOT', 'description': 'GMARO Magazine #11 issue April 2026', 'cover': 'cover.jpg', 'images': ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']},
    {'slug': 'whispers-of-the-fallen', 'title': 'Whispers Of The Fallen', 'folder': 'whispers-of-the-fallen', 'issue': 'ISSUE 09', 'kicker': 'EDITORIAL PHOTOSHOOT', 'description': 'VICTOR Magazine Dubai issue #34', 'cover': 'cover.jpg', 'images': ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg']},
    {'slug': 'untethered', 'title': 'Untethered', 'folder': 'untethered', 'issue': 'ISSUE 15', 'kicker': 'EDITORIAL PHOTOSHOOT', 'description': 'STYLÉCRUZE Magazine June 2026 issue Vol. 204', 'cover': 'cover.jpg', 'images': ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']},
    {'slug': 'luxury-on-the-rocks', 'title': 'Luxury On The Rocks', 'folder': 'luxury-on-the-rocks', 'issue': 'ISSUE 07', 'kicker': 'EDITORIAL PHOTOSHOOT', 'description': 'VOUS Magazine to be published soon', 'cover': 'cover.jpg', 'images': ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg', '10.jpg']},
    {'slug': 'she-is-power', 'title': 'She Is Power', 'folder': 'she-is-power', 'issue': 'ISSUE 13', 'kicker': 'EDITORIAL PHOTOSHOOT', 'description': 'MOEVIR Magazine issue #19 April 2026', 'cover': 'cover.jpg', 'images': ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg']},
    {'slug': 'velvet-society', 'title': 'Velvet Society', 'folder': 'velvet-society', 'issue': 'ISSUE 08', 'kicker': 'EDITORIAL PHOTOSHOOT', 'description': 'MALVIE Magazine June 2026 issue', 'cover': 'cover.jpg', 'images': ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg']},
    {'slug': 'fecc-march', 'title': 'Fecc March', 'folder': 'fecc-march', 'issue': 'ISSUE 05', 'kicker': 'EDITORIAL PHOTOSHOOT', 'description': 'FECC Magazine March 2026 issue', 'cover': 'cover.jpg', 'images': ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg', '10.jpg', '11.jpg']},
    {'slug': 'iconic', 'title': 'Iconic', 'folder': 'iconic', 'issue': 'ISSUE 11', 'kicker': 'EDITORIAL PHOTOSHOOT', 'description': 'QUADRO Magazine', 'cover': 'cover.jpg', 'images': ['1.jpg', '2.jpg', '3.jpg', '4.jpg']},
    {'slug': 'porcelain-hour', 'title': 'Porcelain Hour', 'folder': 'porcelain-hour', 'issue': 'ISSUE 12', 'kicker': 'EDITORIAL PHOTOSHOOT', 'description': 'VOUS Magazine to be published soon', 'cover': 'cover.jpg', 'images': ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']},
    {'slug': 'new-skin', 'title': 'New Skin', 'folder': 'new-skin', 'issue': 'ISSUE 03', 'kicker': 'EDITORIAL PHOTOSHOOT', 'description': 'HIGH VOLT Magazine issue #288 April 2026', 'cover': 'cover.jpg', 'images': ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg']},
    {'slug': 'quiet-flame', 'title': 'Quiet Flame', 'folder': 'quiet-flame', 'issue': 'ISSUE 01', 'kicker': 'EDITORIAL PHOTOSHOOT', 'description': 'VANGUARD Magazine #44 Vol. 14 January 2026', 'cover': 'cover.jpg', 'images': ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg']},
    {'slug': 'no-more-hiding', 'title': 'No More Hiding', 'folder': 'no-more-hiding', 'issue': 'ISSUE 02', 'kicker': 'EDITORIAL PHOTOSHOOT', 'description': 'BLISS Magazine issue Vol. 5 March 2025', 'cover': 'cover.jpg', 'images': ['1.jpg', '2.jpg', '3.jpg', '4.jpg']},
    {'slug': 'rising-within', 'title': 'Rising Within', 'folder': 'rising-within', 'issue': 'ISSUE 04', 'kicker': 'EDITORIAL PHOTOSHOOT', 'description': 'BEAUTICA Magazine issue #2 March 2026', 'cover': 'cover.jpg', 'images': ['1.jpg', '2.jpg', '3.jpg', '4.jpg']}
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


if __name__ == "__main__":
    app.run(debug=True)
