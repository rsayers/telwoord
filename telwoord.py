# coding: UTF-8

"""
Convert numbers into their Dutch written form.
"""

from __future__ import unicode_literals

try:
    unicode
except NameError:
    # Python 3
    unicode = str

UNITS = [
    "nul", "een", "twee", "drie", "vier", "vijf", "zes", "zeven",
    "acht", "negen", "tien", "elf", "twaalf", "dertien", "veertien",
    "vijftien", "zestien", "zeventien", "achttien", "negentien"]

TENS = [
    None, "tien", "twintig", "dertig", "veertig", "vijftig", "zestig",
    "zeventig", "tachtig", "negentig"]

MILLION = 10 ** 6
BILLION = 10 ** 9


def cardinal(n, friendly=True):

    # Use various heuristics for "friendly" results by default.

    if friendly:
    # getallen tot twintig: twee, negen, zeventien, achtste;
    # tientallen tot honderd: twintig, vijftig, tachtigste;
    # honderdtallen tot duizend: driehonderd, negenhonderd;
    # duizendtallen tot twaalfduizend: zesduizend, tienduizendste;
    # de woorden miljoen, miljard, biljoen, enz.: vier miljoen
        if n < 20:
            return cardinal(n, friendly=False)

        if n < 100 and n % 10 == 0:
            return cardinal(n, friendly=False)

        if n < 1000 and n % 100 == 0:
            return cardinal(n, friendly=False)

        if n < 12000 and n % 1000 == 0:
            return cardinal(n, friendly=False)

        if n < MILLION:
            q, r = divmod(n, 1000)
            if r == 0:
                return "%d duizend" % q

        if n < BILLION:
            q, r = divmod(n, MILLION)
            if r == 0:
                return "%d miljoen" % q

        return unicode(n)

    # Code below completely spells out each number.

    if n < 0:
        return "min " + cardinal(abs(n))

    if n < 20:
        return UNITS[n]

    if n < 100:
        q, r = divmod(n, 10)
        a = TENS[q]
        if r == 0:
            return a
        b = cardinal(r)
        joiner = "en" if not b.endswith("e") else "ën"
        return b + joiner + a

    if n < 1000:
        q, r = divmod(n, 100)
        a = cardinal(q, friendly=False) if q > 1 else ""
        b = cardinal(r, friendly=False) if r > 0 else ""
        return a + "honderd" + b

    if 1000 < n < 10000 and n % 1000:
        # Special case for numbers that are exactly divisble by 100, but
        # not by 1000, e.g. "tweeëntwintighonderd"
        q, r = divmod(n, 100)
        if r == 0:
            a = cardinal(q, friendly=False) if q > 1 else ""
            return a + "honderd"

    if n < MILLION:
        q, r = divmod(n, 1000)
        a = cardinal(q, friendly=False) if q > 1 else ""
        b = " " + cardinal(r, friendly=False) if r > 0 else ""
        return a + "duizend" + b

    if n < BILLION:
        q, r = divmod(n, MILLION)
        a = cardinal(q, friendly=False)
        b = " " + cardinal(r, friendly=False) if r > 0 else ""
        return a + " miljoen" + b

    # Fallback to numerical representation
    return unicode(n)


def ordinal(n):
    raise NotImplementedError("Ordinal numbers not yet implemented")


# Aliases

hoofd = n = cardinal
rang = nth = ordinal
