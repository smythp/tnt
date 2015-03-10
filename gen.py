#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

buzz_nouns_singular = [
    "block chain",
    "wearable",
    "big data",
    "Millennial",
    "Internet Of Things",
    "darkweb",
    "deep web",
    "omnichannel retailing",
    "neuromorphics",
    "algorithm",
    "analytics",
    "analysis",
    "best practices",
    "event Horizon",
    "retro",
    "catalytic",
    "solution",
    "dynamic",
    "7g",
]

computer_adjectives = [
    "minimal",
    "neural",
    "synaptic",
    "solid state",
    "asymptotic",
    "concurrent",
    "multithreaded",
    "augmented",
    "presingularity",
    "responsive",
    "Cartesian",
    "extreme",
    "critical",
    "Matrioshka",
    "meatspace",
    "trinary",
    "recursive",
    "Pythonic",
    "functional",
    "imperitive",
    "backend",
    "trontend",
    "social",
    "bio",
    "strategic",
    "sustainable",
    "value added",
    "holistic",
    "nano",
    "granular",
    "cloud",
    "content",
    "core",
    "brick-and-mortar",
    "digital",
    "cyber",
    "geodesic",
    "colocal",
    "electronic",
    "transcendant",
    "programatic",
    "media agnostic",
    "immersive",
    "technocratic",
    "AI",
    "VC",
    "procedural",
    "effective",
    "full spectrum",
    "analytic",
    "peer-to-peer",
    "b2b",
    "semiotic",
    "best practice",
    "new",
    "viral",
    "zero-sum",
    "maker",
    "convergence",
    ]

currency = [
    "Dollar",
    "Cent",
    "Livre",
    "Ducat",
    "buck",
    "Deutschmark",
    "Euro",
    "coin",
    "wampum",
    "porkbelly",
    "future",
    "bond",
    "equity",
    ]

computer_prefixes = [
    "neo",
    "net",
    "geo",
    "crypto",
    "info",
    "digi",
    "tele",
    "cyber",
    "compu",
    "meta",
    "hyper",
    "q-",
    "e-",
    "i",
    "micro",
    "ether",
    "macro",
    "mecha",
    "neuro",
    "tech",
    "x-",
    "stegano,"
    "click",
    "pheno",
]

biparte_nouns = [
    "optics",
    "ops",
    "local",
    "drone",
    "vector",
    "graphy,"
    "hacker",
    "blog",
    "speech",    
    "management",
    "design",
    "tech",
    "nocracy",
    "selfie",
    ]

biparte_adjectives = [
    "service",
    "dendritic",
    "centric",
    "focused",
    "morphic",
    "dermic",
    "sphere",
    "desic",
    "logical",
    "thermic",
    "nomic",
    "factor",
    ]


buzz_gerund = [
    "computing",
    "making",
    "dog fooding",
    "growth hacking",
    "newsjacking",
    "deep linking",
    ]

politician = [
    "Hillary Clinton",
    "Barack Obama",
    "Arnold Schwarzenegger",
    "Mitt Romney",
    "Paul Ryan",
    "Sarah Palin",
    "Queen Rania Al Abdullah",
    "Bill Clinton",
    "Goodluck Jonathan",
    "Mike Huckabee",
    "Herman Cain",
    "Nicolas Sarkozy",
    ]

p_modifier = [
    "Mecha",
    "Cyber",
    "Cyborg",
    "Zombie",
    "Posthuman",
    "Pandimensional",
    "3-D",
]

post = [
    "Prime Minister",
    "President",
    "Senator",
    "Chairman",
    "Representative",
    "Hegemon",
    "General",
    "Secretary",
    ]

s_modifier = [
    " 2.0",
    " Prime",
    "++",
    " Bot",
    ]

def create_politico(politician,p_modifier,s_modifier):
    lenall = len(p_modifier) + len(s_modifier)
    if random.randint(0,lenall) >= len(p_modifier):
        finalpol = ("%s %s" % (random.choice(politician),random.choice(s_modifier)))
    else:
        finalpol = ("%s %s" % (random.choice(p_modifier),random.choice(politician)))
    return(finalpol)

#print("Can %s curb fluctuations in the %s%s market?" % (create_politico(politician,p_modifier,s_modifier),random.choice(computer_prefixes),random.choice(currency)))
    
print("Are %s%s %ss disrupting %s %s in the %s space?" % (random.choice(computer_prefixes),random.choice(biparte_nouns),random.choice(buzz_nouns_singular),random.choice(computer_adjectives),random.choice(buzz_nouns_singular),random.choice(buzz_gerund)))
