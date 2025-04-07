# 🇮🇳 DIGIPIN API – Developed by India Post

DIGIPIN (Digital PIN) is a 10-character alphanumeric geocode developed by the Department of Posts, India. It encodes high-precision geographic coordinates into a compact, user-friendly code and can also be decoded back to latitude/longitude.

This open-source Node.js project exposes a public API to generate and decode DIGIPINs. Intended for use in geolocation services, postal logistics, and spatial analysis.

---

## 🏛️ About DIGIPIN

The Department of Posts has undertaken an initiative to establish a Digital Public Infrastructure (DPI) for a standardized, geo-coded addressing system in India. As a part of this initiative, the Department is releasing the final version of DIGIPIN – the foundation layer of the DPI.

DIGIPIN is an open-source national-level addressing grid developed by the Department of Posts in collaboration with IIT Hyderabad and NRSC, ISRO. It serves as a key component of the digital address ecosystem.

After extensive public consultation and expert review, the DIGIPIN Grid has been finalized to provide simplified addressing solutions for seamless delivery of public and private services and enable “Address as a Service” (AaaS) across the country.

Key highlights of DIGIPIN:

- A uniform offline/online address referencing framework for logical, precise location identification
- Enables GIS integration, bridging the gap between physical and digital addresses
- Supports digitalization of service delivery across sectors such as emergency response, e-commerce, logistics, BFSI (Banking, Financial Services & Insurance), and governance
- Aligns with the National Geospatial Policy 2022, enriching India’s geospatial knowledge stack

DIGIPIN simplifies address management and enhances service delivery accuracy, promoting a thriving geospatial ecosystem for India's digital economy.

---

## ✨ Features

- Encode latitude and longitude into a 10-character DIGIPIN
- Decode a DIGIPIN to its center-point coordinates
- Lightweight, fast, and precise
- RESTful API with interactive Swagger documentation
- Built using Node.js and Express

---

## 📦 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/CEPT-VZG/digipin.git
cd digipin-api
