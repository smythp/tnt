#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Import "random" library
import random

# Create word lists by part of speech
buzz_nouns_singular = [
    "block chain",
    "wearable",
    "big data",
    "Millennial",
    "thingspace",
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
    "mono",
    "uni",
    "duplo",
    "curve",
    "cloud",
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
    "stegano",
    "click",
    "pheno",
]

biparte_nouns = [
    "optics",
    "ops",
    "local",
    "drone",
    "vector",
    "graphy",
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

hashtags = [
    '#technology',
    '#futurism',
    '#innovation',
    '#strategics',
    '#digital',
    '#tech',
    '#future',
    '#analytics',
    '#b2b',
    '#BigData',
    '#data',
    '#business',
    '#cloud',
    '#contextmarketing',
    '#convergence',
    '#crm',
    '#epic',
    '#ftw',
    '#unfail',
    '#FCoE',
    '#thoughtleader',
    '#management',
    '#marketing',
    '#news',
    '#PredictiveAnalytics',
    '#SAP',
    '#SCRM',
    '#SEO',
    '#strategy',
    '#upandcoming',
    '#virtualization',
    '#webdev',
    '#whitepaper',
    ]

# Define a function for each template
# These functions take words and randomly put them into preset sentences
# Note that I didn't use the first one
def create_politico(politician,p_modifier,s_modifier):
    lenall = len(p_modifier) + len(s_modifier)
    if random.randint(0,lenall) >= len(p_modifier):
        finalpol = ("%s %s" % (random.choice(politician),random.choice(s_modifier)))
    else:
        finalpol = ("%s %s" % (random.choice(p_modifier),random.choice(politician)))
    return(finalpol)

# Use print instead of text file write (for testing)
# Notice this is commented out
    
#print("Can %s curb fluctuations in the %s%s market?" % (create_politico(politician,p_modifier,s_modifier),random.choice(computer_prefixes),random.choice(currency)))


def disrupt_gen():
    return("Are %s%s %ss disrupting %s %ss in the %s space?" % (random.choice(computer_prefixes),random.choice(biparte_nouns),random.choice(buzz_nouns_singular),random.choice(computer_adjectives),random.choice(buzz_nouns_singular),random.choice(buzz_gerund)))

def cur_gen():
    return("Are %s%ss the new %s%ss?" % (random.choice(computer_prefixes),random.choice(currency).lower(),random.choice(computer_prefixes),random.choice(currency).lower()))

def problem_gen():
    return("The problem with %s%ss" % (random.choice(computer_prefixes).lower(),random.choice(biparte_nouns).lower()))

    
def future_gen():
    return("%s%s: The future of %s %s?" % (random.choice(computer_prefixes).title(),random.choice(biparte_nouns),random.choice(computer_adjectives),random.choice(buzz_gerund)))

#def hack_gen():
#    print("%sfounders hack %s with a simple %s) % ())

# This function randonly picks one of the above templates
# and and rcalls it to create a sentence
def generate_sentence():
    rolldice = random.randint(0,3)
    if rolldice == 0:
        return disrupt_gen()
    if rolldice == 1:
        return cur_gen()
    if rolldice == 2:
        return future_gen()
    if rolldice == 3:
        return problem_gen()

        
#print(generate_sentence())

tfile = open("tweets.txt", 'w')

# Create variable for the site name and a random buzzword hashtag
site = "technocracynewstoday.com"
hashtag1 = " #" + random.choice(computer_prefixes) + random.choice(biparte_nouns)


#sen1 = generate_sentence() + " " + site + hashtag1
#print(sen1)
#print(len(sen1))

# Wites 100 tweets to tweets.py
# If there's room, also adds two more hashtags to the tweet
# The /n creates a new line. 
for numtweets in range(0,100):
    hashtag1 = " #" + random.choice(computer_prefixes) + random.choice(biparte_nouns)
    sen1 = (generate_sentence() + " " + site + hashtag1)
    for limiting1 in range(0,2):
        hashtag2 = random.choice(hashtags)
        if len(sen1) + len(hashtag2) > 138:
            break
        else:
            sen1 = sen1 + " " + hashtag2
    tfile.write(sen1)
    tfile.write("\n")

tfile.close()

# Can sparkstrea survive chaosmonkey?
