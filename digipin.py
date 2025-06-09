"""
DIGIPIN Encoder and Decoder Library
Developed by India Post, Department of Posts
Released under an open-source license for public use

This module contains two main functions:
 - get_digipin(lat, lon): Encodes latitude & longitude into a 10-digit alphanumeric DIGIPIN
 - get_lat_lng_from_digipin(digi_pin): Decodes a DIGIPIN back into its central latitude & longitude
"""

DIGIPIN_GRID = [
    ['F', 'C', '9', '8'],
    ['J', '3', '2', '7'],
    ['K', '4', '5', '6'],
    ['L', 'M', 'P', 'T']
]

BOUNDS = {
    'minLat': 2.5,
    'maxLat': 38.5,
    'minLon': 63.5,
    'maxLon': 99.5
}

def get_digipin(lat, lon):
    """
    Encodes latitude and longitude into a 10-digit alphanumeric DIGIPIN.

    Args:
        lat (float): Latitude.
        lon (float): Longitude.

    Returns:
        str: The 10-digit alphanumeric DIGIPIN.

    Raises:
        ValueError: If latitude or longitude is out of the defined bounds.
    """
    if not (BOUNDS['minLat'] <= lat <= BOUNDS['maxLat']):
        raise ValueError('Latitude out of range')
    if not (BOUNDS['minLon'] <= lon <= BOUNDS['maxLon']):
        raise ValueError('Longitude out of range')

    min_lat = BOUNDS['minLat']
    max_lat = BOUNDS['maxLat']
    min_lon = BOUNDS['minLon']
    max_lon = BOUNDS['maxLon']

    digi_pin = ''

    for level in range(1, 11):  # Loop from 1 to 10
        lat_div = (max_lat - min_lat) / 4
        lon_div = (max_lon - min_lon) / 4

        # REVERSED row logic (to match original)
        row = 3 - int((lat - min_lat) / lat_div)
        col = int((lon - min_lon) / lon_div)

        row = max(0, min(row, 3))
        col = max(0, min(col, 3))

        digi_pin += DIGIPIN_GRID[row][col]

        if level == 3 or level == 6:
            digi_pin += '-'

        # Update bounds (reverse logic for row)
        max_lat = min_lat + lat_div * (4 - row)
        min_lat = min_lat + lat_div * (3 - row)

        min_lon = min_lon + lon_div * col
        max_lon = min_lon + lon_div
        
    return digi_pin

def get_lat_lng_from_digipin(digi_pin):
    """
    Decodes a DIGIPIN back into its central latitude and longitude.

    Args:
        digi_pin (str): The 10-digit alphanumeric DIGIPIN.

    Returns:
        tuple: A tuple containing the central latitude and longitude (lat, lon).

    Raises:
        ValueError: If the DIGIPIN is invalid or out of range.
    """
    clean_digi_pin = digi_pin.replace('-', '')
    if len(clean_digi_pin) != 10:
        raise ValueError('Invalid DIGIPIN length after removing hyphens. Expected 10 alphanumeric characters.')

    # Reverse lookup for DIGIPIN_GRID to get row and column
    # Create a reverse mapping for faster lookup
    reverse_grid = {}
    for r_idx, row_vals in enumerate(DIGIPIN_GRID):
        for c_idx, char_val in enumerate(row_vals):
            reverse_grid[char_val] = (r_idx, c_idx)

    min_lat = BOUNDS['minLat']
    max_lat = BOUNDS['maxLat']
    min_lon = BOUNDS['minLon']
    max_lon = BOUNDS['maxLon']

    for level in range(1, 11):
        char = clean_digi_pin[level - 1]
        if char not in reverse_grid:
            raise ValueError(f"Invalid character '{char}' in DIGIPIN at level {level}.")

        row, col = reverse_grid[char]

        lat_div = (max_lat - min_lat) / 4
        lon_div = (max_lon - min_lon) / 4

        # Reconstruct bounds based on row and col for decoding
        # The logic here is essentially the reverse of the encoding update
        new_min_lat_for_level = min_lat + lat_div * (3 - row) # Corrected logic
        new_max_lat_for_level = min_lat + lat_div * (4 - row) # Corrected logic

        new_min_lon_for_level = min_lon + lon_div * col
        new_max_lon_for_level = min_lon + lon_div * (col + 1)
        
        min_lat = new_min_lat_for_level
        max_lat = new_max_lat_for_level
        min_lon = new_min_lon_for_level
        max_lon = new_max_lon_for_level

    # Calculate the center of the final grid
    center_lat = min_lat + (max_lat - min_lat) / 2
    center_lon = min_lon + (max_lon - min_lon) / 2

    return center_lat, center_lon

# Example usage:
if __name__ == "__main__":
    # Example coordinates
    
    # latitude = 30.136939161327014
    # longitude = 74.20418057730033
    
    latitude = 28.6139
    longitude = 77.2090


    # Get DIGIPIN
    digipin = get_digipin(latitude, longitude)
    print(f"DIGIPIN for ({latitude}, {longitude}): {digipin}")

    # Decode back to coordinates
    decoded_lat, decoded_lon = get_lat_lng_from_digipin(digipin)
    print(f"Decoded coordinates from DIGIPIN '{digipin}': ({decoded_lat}, {decoded_lon})")