/**
 * DIGIPIN Encoder and Decoder Library
 * Developed by India Post, Department of Posts
 * Released under an open-source license for public use
 *
 * This module contains two main functions:
 *  - getDigiPin(lat, lon): Encodes latitude & longitude into a 10-digit alphanumeric DIGIPIN
 *  - getLatLngFromDigiPin(digiPin): Decodes a DIGIPIN back into its central latitude & longitude
 */

const DIGIPIN_GRID = [
    ['F', 'C', '9', '8'],
    ['J', '3', '2', '7'],
    ['K', '4', '5', '6'],
    ['L', 'M', 'P', 'T']
  ];
  
  const BOUNDS = {
    minLat: 2.5,
    maxLat: 38.5,
    minLon: 63.5,
    maxLon: 99.5
  };
  
  function getDigiPin(lat, lon) {
    if (lat < BOUNDS.minLat || lat > BOUNDS.maxLat) throw new Error('Latitude out of range');
    if (lon < BOUNDS.minLon || lon > BOUNDS.maxLon) throw new Error('Longitude out of range');
  
    let minLat = BOUNDS.minLat;
    let maxLat = BOUNDS.maxLat;
    let minLon = BOUNDS.minLon;
    let maxLon = BOUNDS.maxLon;
  
    let digiPin = '';
  
    for (let level = 1; level <= 10; level++) {
      const latDiv = (maxLat - minLat) / 4;
      const lonDiv = (maxLon - minLon) / 4;
  
      let row = Math.floor((lat - minLat) / latDiv);
      let col = Math.floor((lon - minLon) / lonDiv);
  
      row = Math.min(row, 3);
      col = Math.min(col, 3);
  
      digiPin += DIGIPIN_GRID[row][col];
  
      if (level === 3 || level === 6) digiPin += '-';
  
      maxLat = minLat + latDiv * (row + 1);
      minLat = minLat + latDiv * row;
  
      minLon = minLon + lonDiv * col;
      maxLon = minLon + lonDiv;
    }
  
    return digiPin;
  }
  
  function getLatLngFromDigiPin(digiPin) {
    const pin = digiPin.replace(/-/g, '');
    if (pin.length !== 10) throw new Error('Invalid DIGIPIN');
  
    let minLat = BOUNDS.minLat;
    let maxLat = BOUNDS.maxLat;
    let minLon = BOUNDS.minLon;
    let maxLon = BOUNDS.maxLon;
  
    for (let i = 0; i < 10; i++) {
      let found = false;
      const char = pin[i];
      for (let r = 0; r < 4; r++) {
        for (let c = 0; c < 4; c++) {
          if (DIGIPIN_GRID[r][c] === char) {
            const latDiv = (maxLat - minLat) / 4;
            const lonDiv = (maxLon - minLon) / 4;
  
            const newMinLat = minLat + latDiv * r;
            const newMaxLat = minLat + latDiv * (r + 1);
            const newMinLon = minLon + lonDiv * c;
            const newMaxLon = minLon + lonDiv * (c + 1);
  
            minLat = newMinLat;
            maxLat = newMaxLat;
            minLon = newMinLon;
            maxLon = newMaxLon;
  
            found = true;
            break;
          }
        }
        if (found) break;
      }
      if (!found) throw new Error('Invalid character in DIGIPIN');
    }
  
    const centerLat = (minLat + maxLat) / 2;
    const centerLon = (minLon + maxLon) / 2;
    return { latitude: centerLat.toFixed(6), longitude: centerLon.toFixed(6) };
  }
  
  // Export for node.js or browser
  if (typeof module !== 'undefined') module.exports = { getDigiPin, getLatLngFromDigiPin };
  