def validate_sector(sector: str):
    if not sector.isalpha():
        return False
    
    if len(sector) < 3 or len(sector) > 30:
        return False

    return True