from flask import Flask, render_template, abort

app = Flask(__name__)

stylist = {
    "name": "Elizabet Filippenko",
    "intro": "Selected styling portfolio and editorial projects.",
    "bio": "A fashion styling portfolio featuring editorial shoots, visual storytelling, and selected creative works.",
}

stories = [
    {
        "slug": "quiet-flame",
        "title": "Quiet Flame",
        "folder": "quiet-flame",
        "issue": "ISSUE 01",
        "kicker": "EDITORIAL",
        "description": "A bold editorial story with clean silhouettes and strong mood.",
        "cover": "cover.jpg",
        "images": ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg", "6.jpg"],
    },
    {
        "slug": "no-more-hiding",
        "title": "No More Hiding",
        "folder": "no-more-hiding",
        "issue": "ISSUE 02",
        "kicker": "EDITORIAL",
        "description": "A fashion story focused on confidence, attitude, and visual contrast.",
        "cover": "cover.jpg",
        "images": ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"],
    },
    {
        "slug": "new-skin",
        "title": "New Skin",
        "folder": "new-skin",
        "issue": "ISSUE 03",
        "kicker": "PORTFOLIO",
        "description": "A portfolio series with sculptural poses and modern editorial styling.",
        "cover": "cover.jpg",
        "images": ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg", "6.jpg", "7.jpg"],
    },
    {
        "slug": "rising-within",
        "title": "Rising Within",
        "folder": "rising-within",
        "issue": "ISSUE 04",
        "kicker": "PORTFOLIO",
        "description": "A clean and expressive beauty-fashion story with a strong cover moment.",
        "cover": "cover.jpg",
        "images": ["1.jpg", "2.jpg", "3.jpg", "4.jpg"],
    },
    {
        "slug": "fecc-march",
        "title": "Fecc March",
        "folder": "fecc march",
        "issue": "ISSUE 05",
        "kicker": "EDITORIAL",
        "description": "An editorial lineup with layered looks and a magazine-style mood.",
        "cover": "cover.jpg",
        "images": ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg", "6.jpg", "7.jpg", "8.jpg", "9.jpg", "10.jpg", "11.jpg"],
    },
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
    app.run(debug=True)    {
        "slug": "shoot-06",
        "title": "Shoot 06",
        "folder": "shoot-06",
        "issue": "ISSUE 06",
        "kicker": "PORTFOLIO",
        "description": "Preview description.",
        "cover": "cover.jpg",
        "images": ["1.jpg", "2.jpg", "3.jpg", "4.jpg"],
    },
    {
        "slug": "shoot-07",cat > app.py <<'EOF'
from flask import Flask, render_template, abort

app = Flask(__name__)

stylist = {
    "name": "Elizabet Filippenko",
    "intro": "Selected styling portfolio and editorial projects.",
    "bio": "A fashion styling portfolio featuring editorial shoots, visual storytelling, and selected creative works.",
}

stories = [
    {
        "slug": "quiet-flame",
        "title": "Quiet Flame",
        "folder": "quiet-flame",
        "issue": "ISSUE 01",
        "kicker": "EDITORIAL",
        "description": "A bold editorial story with clean silhouettes and strong mood.",
        "cover": "cover.jpg",
        "images": ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg", "6.jpg"],
    },
    {
        "slug": "no-more-hiding",
        "title": "No More Hiding",
        "folder": "no-more-hiding",
        "issue": "ISSUE 02",
        "kicker": "EDITORIAL",
        "description": "A fashion story focused on confidence, attitude, and visual contrast.",
        "cover": "cover.jpg",
        "images": ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"],
    },
    {
        "slug": "new-skin",
        "title": "New Skin",
        "folder": "new-skin",
        "issue": "ISSUE 03",
        "kicker": "PORTFOLIO",
        "description": "A portfolio series with sculptural poses and modern editorial styling.",
        "cover": "cover.jpg",
        "images": ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg", "6.jpg", "7.jpg"],
    },
    {
        "slug": "rising-within",
        "title": "Rising Within",
        "folder": "rising-within",
        "issue": "ISSUE 04",
        "kicker": "PORTFOLIO",
        "description": "A clean and expressive beauty-fashion story with a strong cover moment.",
        "cover": "cover.jpg",
        "images": ["1.jpg", "2.jpg", "3.jpg", "4.jpg"],
    },
    {
        "slug": "fecc-march",
        "title": "Fecc March",
        "folder": "fecc march",
        "issue": "ISSUE 05",
        "kicker": "EDITORIAL",
        "description": "An editorial lineup with layered looks and a magazine-style mood.",
        "cover": "cover.jpg",
        "images": ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg", "6.jpg", "7.jpg", "8.jpg", "9.jpg", "10.jpg", "11.jpg"],
    },
    {
        "slug": "shoot-06",
        "title": "Shoot 06",
        "folder": "shoot-06",
        "issue": "ISSUE 06",
        "kicker": "PORTFOLIO",
        "description": "Preview description.",
        "cover": "cover.jpg",
        "images": ["1.jpg", "2.jpg", "3.jpg", "4.jpg"],
    },
    {
        "slug": "shoot-07",
        "title": "Shoot 07",
        "folder": "shoot-07",
        "issue": "ISSUE 07",
        "kicker": "PORTFOLIO",
        "description": "Preview description.",
        "cover": "cover.jpg",
        "images": ["1.jpg", "2.jpg", "3.jpg", "4.jpg"],
    },
    {
        "slug": "shoot-08",
        "title": "Shoot 08",
        "folder": "shoot-08",
        "issue": "ISSUE 08",
        "kicker": "PORTFOLIO",
        "description": "Preview description.",
        "cover": "cover.jpg",
        "images": ["1.jpg", "2.jpg", "3.jpg", "4.jpg"],
    },
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
EOF

        "title": "Shoot 07",
cd ~/fashion_portfolio
        "folder": "shoot-07",python3 app.py
        
        "issue": "ISSUE 07",
        "kicker": "PORTFOLIO",
        "description": "Preview description.",
        "cover": "cover.jpg",
        "images": ["1.jpg", "2.jpg", "3.jpg", "4.jpg"],
    },
    {
        "slug": "shoot-08",
        "title": "Shoot 08",
        "folder": "shoot-08",
        "issue": "ISSUE 08",
        "kicker": "PORTFOLIO",
        "description": "Preview description.",
        "cover": "cover.jpg",
        "images": ["1.jpg", "2.jpg", "3.jpg", "4.jpg"],stories = [
            
    },
