from . import __version__


config = {
    "userAgent": f"OuafIntranet {__version__}",

    "service": {
        "BASE_URL": "https://iut-rcc-intranet.univ-reims.fr/fr"
    },

    "cas": {
        "BASE_URL": "https://cas.univ-reims.fr/cas/login"
    },

}
