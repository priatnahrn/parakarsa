{
    "name": "Parakarsa",
    "version": "1.0.0",
    "category": "Website",
    "author": "Parakarsa",
    "summary": "Parakarsa is a co-creation platform for UMKM",
    "website": "https://parakarsa.com",
    "depends": ["website"],
    "data": [
        "views/pages/landing.xml",
        "views/pages/events.xml",
        "views/pages/event_detail.xml",
        "views/pages/about_us.xml",
        "views/pages/coming_soon.xml",
        "views/components/navbar.xml",
        "views/components/footer.xml",
    ],

    "assets": {
        "web.assets_frontend": [
            "parakarsa/static/src/css/styles.css",
            "parakarsa/static/src/js/navbar.js",
            "parakarsa/static/src/js/events.js",
            "parakarsa/static/src/js/event_detail.js",
            "parakarsa/static/src/css/home.css",
            "parakarsa/static/src/css/about.css",
            "parakarsa/static/src/css/events.css",
            "parakarsa/static/src/js/home.js",
        ],
    },
    "application": False,
}
