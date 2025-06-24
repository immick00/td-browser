import random
import json
from patchright.async_api import BrowserContext

def get_random_resolution():
    common_resolutions = [
        {"width": 3840, "height": 2160},
        {"width": 3440, "height": 1440},
        {"width": 2560, "height": 1440},
        {"width": 2560, "height": 1080},
        {"width": 1920, "height": 1200},
        {"width": 1920, "height": 1080},
        {"width": 1680, "height": 1050},
        {"width": 1600, "height": 900},
        {"width": 1440, "height": 900},
        {"width": 1366, "height": 768},
        {"width": 1280, "height": 1024},
        {"width": 1280, "height": 800},
        {"width": 1024, "height": 768}
    ]
    return random.choice(common_resolutions)

async def inject_browser_js(context: BrowserContext, width, height):
    hardware_concurrency = random.choice([4, 8, 6, 12, 16])
    device_pixel_ratio = random.choice([1, 1.5, 1.75, 2])

    js_script = f"""
            Object.defineProperty(navigator, 'deviceMemory', {{
                get: () => 8 
            }});

            Object.defineProperty(navigator, 'hardwareConcurrency', {{
                get: () => {hardware_concurrency} 
            }});

            Object.defineProperty(screen, 'availWidth', {{
                get: () => {width},
            }});

            Object.defineProperty(screen, 'availHeight', {{
                get: () => {height - random.randrange(90)},
            }});

            Object.defineProperty(window, 'outerWidth', {{
                get: () => {width},
            }});

            Object.defineProperty(window, 'outerHeight', {{
                get: () => {height - random.randrange(140)},
            }});

            Object.defineProperty(window, 'devicePixelRatio', {{
                get: () => {device_pixel_ratio},
            }});
        """

    await context.add_init_script(js_script)

def get_random_gpu():
    with open("gpus.json", "r", encoding="utf-8") as f:
        content = f.read()
    gpus = json.loads(content)
    gpu = random.choice(gpus)

    unmasked_vendor = gpu["webgl"][0]["webgl_unmasked_vendor"]
    unmasked_renderer = gpu["webgl"][0]["webgl_unmasked_renderer"]


    return f"{unmasked_vendor}-&-{unmasked_renderer}"

def get_random_timezone():
    timezones = [
        "America/Adak",
        "America/Anchorage",
        "America/Anguilla",
        "America/Antigua",
        "America/Araguaina",
        "America/Aruba",
        "America/Asuncion",
        "America/Bahia",
        "America/Bahia_Banderas",
        "America/Barbados",
        "America/Belem",
        "America/Blanc-Sablon",
        "America/Boa_Vista",
        "America/Boise",
        "America/Buenos_Aires",
        "America/Cambridge_Bay",
        "America/Campo_Grande",
        "America/Cancun",
        "America/Catamarca",
        "America/Cayenne",
        "America/Cayman",
        "America/Chicago",
        "America/Chihuahua",
        "America/Ciudad_Juarez",
        "America/Coral_Harbour",
        "America/Cordoba",
        "America/Coyhaique",
        "America/Creston",
        "America/Cuiaba",
        "America/Curacao",
        "America/Danmarkshavn",
        "America/Dawson",
        "America/Dawson_Creek",
        "America/Denver",
        "America/Detroit",
        "America/Dominica",
        "America/Edmonton",
        "America/Eirunepe",
        "America/Fort_Nelson",
        "America/Fortaleza",
        "America/Glace_Bay",
        "America/Godthab",
        "America/Goose_Bay",
        "America/Grand_Turk",
        "America/Grenada",
        "America/Guadeloupe",
        "America/Guayaquil",
        "America/Guyana",
        "America/Halifax",
        "America/Hermosillo",
        "America/Indiana/Knox",
        "America/Indiana/Marengo",
        "America/Indiana/Petersburg",
        "America/Indiana/Tell_City",
        "America/Indiana/Vevay",
        "America/Indiana/Vincennes",
        "America/Indiana/Winamac",
        "America/Indianapolis",
        "America/Inuvik",
        "America/Iqaluit",
        "America/Jamaica",
        "America/Jujuy",
        "America/Juneau",
        "America/Kentucky/Monticello",
        "America/Kralendijk",
        "America/Los_Angeles",
        "America/Louisville",
        "America/Lower_Princes",
        "America/Maceio",
        "America/Manaus",
        "America/Marigot",
        "America/Martinique",
        "America/Matamoros",
        "America/Mazatlan",
        "America/Mendoza",
        "America/Menominee",
        "America/Merida",
        "America/Metlakatla",
        "America/Miquelon",
        "America/Moncton",
        "America/Monterrey",
        "America/Montevideo",
        "America/Montserrat",
        "America/Nassau",
        "America/New_York",
        "America/Nome",
        "America/Noronha",
        "America/North_Dakota/Beulah",
        "America/North_Dakota/Center",
        "America/North_Dakota/New_Salem",
        "America/Ojinaga",
        "America/Paramaribo",
        "America/Phoenix",
        "America/Port-au-Prince",
        "America/Port_of_Spain",
        "America/Porto_Velho",
        "America/Puerto_Rico",
        "America/Punta_Arenas",
        "America/Rankin_Inlet",
        "America/Recife",
        "America/Regina",
        "America/Resolute",
        "America/Rio_Branco",
        "America/Santarem",
        "America/Santo_Domingo",
        "America/Sao_Paulo",
        "America/Scoresbysund",
        "America/Sitka",
        "America/St_Barthelemy",
        "America/St_Johns",
        "America/St_Kitts",
        "America/St_Lucia",
        "America/St_Thomas",
        "America/St_Vincent",
        "America/Swift_Current",
        "America/Thule",
        "America/Tijuana",
        "America/Toronto",
        "America/Tortola",
        "America/Vancouver",
        "America/Whitehorse",
        "America/Winnipeg",
        "America/Yakutat"
    ]
    return random.choice(timezones)