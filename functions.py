

def check_type(value):
    product_name = str(value).lower()
    if 'galaxy' in product_name or 'iphone' in product_name or 'xiaomi' in product_name:
        return 'Mobil'
        # Checking for TV-related terms
    elif 'tab' in product_name or 'ipad' in product_name:
        return 'Tablet'
    elif 'ear' in product_name or 'jbl' in product_name:
        return 'Earphones'
    elif 'lg ' in product_name or 'qn' in product_name:
        return 'Televize'