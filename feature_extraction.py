from urllib.parse import urlparse
import re

# Normalize URL
def normalize_url(url):
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    url = url.strip()
    url = re.sub(r'[^\x00-\x7F]+', '', url)  # remove non-ASCII chars
    return url

# Extract features
def extract_features(url):
    try:
        url = normalize_url(url)
        parsed = urlparse(url)
        url_lower = url.lower()

        features = []

        # --- BASIC FEATURES ---
        features.append(len(url))                       # 1 URL length
        features.append(len(parsed.netloc))             # 2 Domain length
        features.append(len(parsed.path))               # 3 Path length
        features.append(url.count('.'))                 # 4 Dot count
        features.append(sum(c.isdigit() for c in url)) # 5 Digit count
        features.append(1 if '@' in url else 0)        # 6 @ symbol
        features.append(1 if '-' in url else 0)        # 7 Hyphen
        features.append(1 if parsed.scheme == 'https' else 0)  # 8 HTTPS

        # --- PHISHING-SPECIFIC FEATURES ---
        features.append(url_lower.count('login'))      # 9
        features.append(url_lower.count('verify'))     # 10
        features.append(url_lower.count('secure'))     # 11
        features.append(url_lower.count('update'))     # 12
        features.append(url.count('?'))                # 13
        features.append(url.count('&'))                # 14
        features.append(url.count('='))                # 15
        features.append(url.count('%'))                # 16
        features.append(len(parsed.netloc.split('.'))) # 17 Subdomains
        features.append(sum(c.isdigit() for c in url)/len(url)) # 18 Digit ratio

        return features

    except Exception as e:
        # --- Fallback: must return EXACTLY 18 features ---
        print(f"Error extracting features from URL {url}: {e}")
        return [0]*18
