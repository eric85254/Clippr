"""
    This is where global constants are stored.
    Default Picture locations and Default Haircut Locations are stored here.
"""
DEFAULT_PICTURE_LOCATION = "\defaults\default_user.png"
DEFAULT_MENU_PICTURE = "\defaults\default_menu.png"

DEFAULT_HAIRCUT_1 = "\defaults\haircut.jpeg"
DEFAULT_HAIRCUT_2 = "\defaults\haircut2.jpeg"
DEFAULT_HAIRCUT_3 = "\defaults\haircut3.jpeg"

DUMMY_STYLIST_PICTURES = {
    'sam_bee': '\defaults\profile_pictures\sam_bee.jpg',
    'samantha_clem': '\defaults\profile_pictures\samantha_clem.jpg',
    'mckenna_kent': '\defaults\profile_pictures\mckenna_kent.jpeg',
    'lindsay_mcgreggor': '\defaults\profile_pictures\lindsay_mcgreggor.jpeg',
    'mariah_han': '\defaults\profile_pictures\mariah_han.jpeg',
    'jacob_rudy': '\defaults\profile_pictures\jacob_rudy.jpeg',
    'alanzo_dominguez': r'\defaults\profile_pictures\alanzo_dominguez.jpeg',
    'lauren_brown': '\defaults\profile_pictures\lauren_brown.jpeg',
    'tina_davina': r'\defaults\profile_pictures\tina_davina.jpeg',
    'linda_xue': '\defaults\profile_pictures\linda_xue.jpeg'
}

DUMMY_PORTFOLIO_PICTURES = {
    'sam_bee': [
        {
            'picture': '\defaults\portfolio_haircuts\sam_bee\haircut1.jpeg',
            'name': 'Braid',
            'description': 'Braid',
            'price': 13.00,
        },
        {
            'picture': '\defaults\portfolio_haircuts\sam_bee\haircut2.jpeg',
            'name': 'Braid',
            'description': 'Elsa Braid',
            'price': 13.00
        },
        {
            'picture': '\defaults\portfolio_haircuts\sam_bee\haircut3.jpeg',
            'name': 'Fancy Braid',
            'description': 'Three styles of beautiful braids',
            'price': 30.00
        }
    ],
    'samantha_clem': [
        {
            'picture': '\defaults\portfolio_haircuts\samantha_clem\haircut1.jpeg',
            'name': 'Style 1',
            'description': 'Braid on top - Pony tail in back',
            'price': 30.00
        },
        {
            'picture': '\defaults\portfolio_haircuts\samantha_clem\haircut2.jpeg',
            'name': 'Style 2',
            'description': "Classic men's cut",
            'price': 14.00
        },
        {
            'picture': '\defaults\portfolio_haircuts\samantha_clem\haircut3.jpeg',
            'name': 'Style 3',
            'description': 'Modern Styled Top Knot',
            'price': 23.00
        }
    ],
    'mckenna_kent': [
        {
            'picture': '\defaults\portfolio_haircuts\mckenna_kent\haircut1.jpeg',
            'name': 'Original',
            'description': "Classic men's style",
            'price': 12.00
        },
        {
            'picture': '\defaults\portfolio_haircuts\haircut2.jpeg',
            'name': 'Original 2',
            'description': "Literally the same as the first one.",
            'price': 13.00
        },
        {
            'picture': '\defaults\portfolio_haircuts\haircut3.jpeg',
            'name': 'Original 3',
            'description': "Classic Top Knot",
            'price': 15.00
        }
    ],
    'lindsay_mcgreggor': [
        {
            'picture': '\defaults\portfolio_haircuts\haircut1.jpeg',
            'name': 'Purple Cut',
            'description': "Modern Pixie Cut",
            'price': 25.00
        },
        {
            'picture': '\defaults\portfolio_haircuts\haircut2.jpeg',
            'name': 'Star Cut',
            'description': 'Classic Runway Model Look',
            'price': 35.00
        },
        {
            'picture': '\defaults\portfolio_haircuts\haircut3.jpeg',
            'name': 'Sexy Pixie Cut',
            'description': 'Short with a new flavor.',
            'price': 40.00
        }
    ],
    'mariah_han': [
        {
            'picture': '\defaults\portfolio_haircuts\mariah_han\haircut1.jpeg',
            'name': 'Bob',
            'description': 'This is the classic "bob for apples" look',
            'price': 32.00
        },
        {
            'picture': '\defaults\portfolio_haircuts\mariah_han\haircut2.jpeg',
            'name': 'Bob 2',
            'description': 'Good enough for an actress? good enough 4 u',
            'price': 50.00
        },
        {
            'picture': '\defaults\portfolio_haircuts\mariah_han\haircut3.jpeg',
            'name': 'Bob 3',
            'description': 'Ole Fashion',
            'price': 15.00
        }
    ],
    'jacob_rudy': [
        {
            'picture': '\defaults\portfolio_haircuts\jacob_rudy\haircut1.jpeg',
            'name': 'Forest Top',
            'description': 'Fresh on the sides, party on the top!',
            'price': 25.00
        },
        {
            'picture': '\defaults\portfolio_haircuts\jacob_rudy\haircut2.jpeg',
            'name': 'Clean as Hell',
            'description': 'Nothing looks fresher than this.',
            'price': 25.00
        },
        {
            'picture': '\defaults\portfolio_haircuts\jacob_rudy\haircut3.jpeg',
            'name': 'Old School Cool',
            'description': 'Fresh and Classic',
            'price': 25.00
        }
    ],
    'alanzo_dominguez': [
        {
            'picture': r'\defaults\portfolio_haircuts\alanzo_dominguez\haircut1.jpeg',
            'name': 'Rowdy Ruben',
            'description': "A more eccentric look",
            'price': 40.00
        },
        {
            'picture': r'\defaults\portfolio_haircuts\alanzo_dominguez\haircut2.jpeg',
            'name': 'Bieber Flow',
            'description': 'Model Look',
            'price': 25.00
        },
        {
            'picture': r'\defaults\portfolio_haircuts\alanzo_dominguez\haircut3.jpeg',
            'name': 'Business',
            'description': 'Perfect look for the newly established business man',
            'price': 40.00
        }
    ],
    'lauren_brown': [
        {
            'picture': '\defaults\portfolio_haircuts\lauren_brown\haircut1.jpeg',
            'name': 'Kim Jong-Un',
            'description': 'Perfect Cut if for those with the dictator mindset',
            'price': 30.00
        },
        {
            'picture': '\defaults\portfolio_haircuts\lauren_brown\haircut2.jpeg',
            'name': 'Abraham Lincoln',
            'description': 'Good ole abe with a fresh twist',
            'price': 40.00
        },
        {
            'picture': '\defaults\portfolio_haircuts\lauren_brown\haircut2.jpeg',
            'name': 'Regular Cut',
            'description': 'Only if you wanna be boring',
            'price': 1.00
        }
    ],
    'tina_davina': [
        {
            'picture': r'\defaults\portfolio_haircuts\tina_davina\haircut1.jpeg',
            'name': 'Fluffy Puffy',
            'description': 'Nice Old School Pern',
            'price': 40.00
        },
        {
            'picture': r'\defaults\portfolio_haircuts\tina_davina\haircut2.jpeg',
            'name': 'Bold and Strong',
            'description': 'Perm meets modern fashion',
            'price': 15.00
        },
        {
            'picture': r'\defaults\portfolio_haircuts\tina_davina\haircut3.jpeg',
            'name': 'Not a Perm!',
            'description': 'Not a perm :(',
            'price': 20.00
        }
    ],
    'linda_xue': [
        {
            'picture': '\defaults\portfolio_haircuts\linda_xue\haircut1.jpeg',
            'name': 'Side Bang',
            'description': 'great for all occasions!',
            'price': 14.00
        },
        {
            'picture': '\defaults\portfolio_haircuts\linda_xue\haircut2.jpeg',
            'name': 'Short Bob',
            'description': 'Short and Sexy',
            'price': 25.00
        },
        {
            'picture': '\defaults\portfolio_haircuts\linda_xue\haircut3.jpeg',
            'name': 'Model Status',
            'description': 'I can turn you into her.',
            'price': 145.00
        }
    ],
}
