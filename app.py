import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# ==========================================
# CENTRAL ADMIN CONFIGURATION
# ==========================================
CONFIG = {
    # Channel Settings
    "CHANNEL_NAME": "VIP Community",
    "TELEGRAM_URL": "https://t.me/+CcZ509YWq1IyMmVl",
    "VERIFIED_BADGE": True,
    
    # Meta / SEO Settings
    "META_TITLE": "Join Our Official Telegram Community",
    "META_DESCRIPTION": "Get exclusive alerts, daily curated resources, and stay ahead with direct community access.",
    
    # Hero Section Copy
    "HERO_SUBTITLE": "Direct VIP Access",
    "HERO_TITLE": "JOIN OUR TELEGRAM CHANNEL",
    "HERO_DESCRIPTION": "Join thousands of active members receiving instant daily updates, premium setups, and community discussions directly on Telegram.",
    "CTA_BUTTON_TEXT": "JOIN TELEGRAM CHANNEL",
    "SECONDARY_BUTTON_TEXT": "Explore Highlights",
    
    # Value Proposition Cards
    "FEATURES": [
        {
            "icon": "fa-bolt-lightning",
            "title": "Real-Time Alerts",
            "desc": "Zero algorithm delays. Receive notifications the second new releases and updates go live."
        },
        {
            "icon": "fa-shield-halved",
            "title": "Verified Quality",
            "desc": "Hand-screened, authentic content with strict anti-spam moderation inside the community."
        },
        {
            "icon": "fa-users",
            "title": "Active Member Network",
            "desc": "Connect with an engaged circle of like-minded members across active discussion threads."
        }
    ],

    # Social Proof Counter Stats
    "STATS": [
        {"count": "45K+", "label": "Subscribers"},
        {"count": "99.8%", "label": "Daily Activity"},
        {"count": "24/7", "label": "Direct Access"}
    ],

    # Advertisement Blocks
    "ADS": {
        # Monetag All-in-One (Multitag) Script
        "TOP_BANNER": """<script src="https://quge5.com/88/tag.min.js" data-zone="307712" async data-cfasync="false"></script>""",
        "BELOW_CTA": None,
        "BOTTOM_BANNER": None
    },

    # Footer Links
    "FOOTER": {
        "COPYRIGHT_YEAR": "2026",
        "CONTACT_URL": "https://t.me/+CcZ509YWq1IyMmVl",
        "DISCLAIMER": "This landing page is an independent community hub and is not affiliated with or endorsed by Telegram FZ-LLC."
    }
}

@app.route("/")
def index():
    return render_template("index.html", config=CONFIG)

# Monetag Verification & Service Worker Route
@app.route("/sw.js")
def service_worker():
    return send_from_directory("static", "sw.js", mimetype="application/javascript")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
