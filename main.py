UNITS = ["zéro", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf", 
         "dix", "onze", "douze", "treize", "quatorze", "quinze", "seize"]

TENS = ["", "dix", "vingt", "trente", "quarante", "cinquante", "soixante", "soixante-dix", "quatre-vingts", "quatre-vingt-dix"]


def convert_units(n):
    return UNITS[n]


def convert_tens(n):
    if n < 17:
        return convert_units(n)
    elif n < 20:
        return "dix-" + UNITS[n - 10]
    elif n < 70:
        if n % 10 == 1 and n != 11:
            return TENS[n // 10] + "-et-un"
        return TENS[n // 10] + (("-" + UNITS[n % 10]) if n % 10 != 0 else "")
    elif n < 80:
        if n == 71:
            return "soixante-et-onze"
        return "soixante-" + convert_tens(n - 60)
    elif n < 100:
        if n == 81:
            return "quatre-vingt-un"
        if n == 91:
            return "quatre-vingt-onze"
        return "quatre-vingt" + (("s" if n == 80 else "") + (("-" + UNITS[n % 10]) if n % 10 != 0 else ""))
    return ""

def convert_hundreds(n):
    if n < 100:
        return convert_tens(n)
    elif n == 100:
        return "cent"
    else:
        return (UNITS[n // 100] + "-cent" + 
                (("s" if n % 100 == 0 and n // 100 > 1 else "") + 
                (("-" + convert_tens(n % 100)) if n % 100 != 0 else "")))

def convert_thousands(n):
    if n < 1000:
        return convert_hundreds(n)
    elif n == 1000:
        return "mille"
    else:
        thousands = n // 1000
        return (convert_hundreds(thousands) + "-mille" + 
                (("-" + convert_hundreds(n % 1000)) if n % 1000 != 0 else ""))

def convert_large_numbers(n):
    if n < 1000000:
        if n < 10000:
            return convert_thousands(n)
        else:
            thousands = n // 1000
            return (convert_thousands(thousands) + "-mille" + 
                    (("-" + convert_hundreds(n % 1000)) if n % 1000 != 0 else ""))
    else:
        millions = n // 1000000
        return (convert_thousands(millions) + "-million" + 
                ("s" if millions > 1 else "") + 
                (("-" + convert_large_numbers(n % 1000000)) if n % 1000000 != 0 else ""))

def number_to_french(n):
    if n < 0:
        raise ValueError("Number must be non-negative")
    elif n < 17:
        return convert_units(n)
    elif n < 100:
        return convert_tens(n)
    elif n < 1000:
        return convert_hundreds(n)
    elif n < 1000000:
        return convert_thousands(n)
    else:
        return convert_large_numbers(n)
