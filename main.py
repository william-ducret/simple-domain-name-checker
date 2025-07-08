

import requests
import whois

# -----------------------------------------------------------
# Parameters
# -----------------------------------------------------------

mode = 3 # chose the mode (1,2 or 3)
# 1 : requests with a list of url
# 1 : requests with a combination of names and ltd
# 1 : whois with a combination of names and ltd


verbose = False # set to True for logginf or debugging purpose

# Mode 1 : enter the urls to check

urls = [
    "https://www.nvdf34kj56.com", 
    "https://www.google.com/",
    ]

# Mode 2 : chose a list of name and tld to check (will chekc all possible combination)

prefixe = "https://www."

names = ["abc", "xyz", "ltd", "hello", "hsk", "ppl", "ppt", "word", "doc", "hello"
         "123", "b2b", "b2c", "pdp", "sms", "hms", "kiwi", "green", "ktv", "mi6"]

tlds = [".com", ".org", ".net", ".info", ".de", ".fr", ".it", ".es", ".uk", 
        ".eu", ".au", ".bb", ".be", ".ca", ".ch", ".fi", ".com", ".li", 
        ".lt", ".lu", ".pl", ".pt", ".pw", ".com", ".pro", ".name", ".me", 
        ".io", ".cloud", ".lol", ".world", ".art", ".app", ".nl", ".yt"]

# Results storage
 
results = []



# -----------------------------------------------------------
# Function
# -----------------------------------------------------------

def url_check(url, verbose):
    if verbose :
        print("- Checking url : ", url)

    try:
        response = requests.get(url, timeout=2)
        response.raise_for_status()  # Lève une exception pour les codes 4xx ou 5xx
        if verbose :
            print("- Connexion successful, existing page")
        result = "Taken"

    except requests.exceptions.HTTPError as e:
        if verbose :
            print("- HTTP error")
        error_msg = e
        result = "HTTP error"
    except requests.exceptions.ConnectionError as e:
        if verbose :
            print("- Impossible to connect, inexistant page")
        error_msg = e
        result = "Available"
    except requests.exceptions.Timeout as e:
        if verbose :
            print("- Timeout")
        error_msg = e
        result = "Timeout"
    except requests.exceptions.RequestException as e:
        if verbose :
            print("- Request error")
        error_msg = e
        result = "Request error"

    return result

def whois_check(url):
    try:
        info = whois.whois(url)
        if info.domain_name:
            return "Existing"
        else:
            return "Available"
    except Exception as e:
        # print(f"Erreur WHOIS : {e}")
        return "Error"

# -----------------------------------------------------------
# Process
# -----------------------------------------------------------

if mode == 1:
    for url in urls:
        r = url_check(url, verbose)
        results.append(r)
elif mode == 2:
    urls = [] # reset urls variable so we can use it
    for name in names:
        for tld in tlds:
            url = prefixe + name + tld
            print(url)
            r = url_check(url, verbose)
            results.append(r)
            urls.append(url)

            print("- ", r)
elif mode == 3:
    urls = [] # reset urls variable so we can use it
    for name in names:
        for tld in tlds:
            url = prefixe + name + tld
            print(url)
            r = whois_check(url)
            print("- ", r)
else:
    print("- mode not existing, please change mode")


print("- Result : ")
print("--------------------------")
print(results)
