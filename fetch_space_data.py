from astroquery.gaia import Gaia
import astropy.units as u
from astropy.coordinates import SkyCoord
import json

print("Connecting to Gaia DR3 archive to fetch real stars...")
coord = SkyCoord(ra=56.75 * u.deg, dec=24.11 * u.deg, frame='icrs')
job = Gaia.query_object_async(coordinate=coord, width=0.3*u.deg, height=0.3*u.deg)

print(f"Retrieved {len(job)} real stars successfully!")

stars = []
for i in range(min(50, len(job))):
    stars.append({
        "id": i,
        "x": float(job['ra'][i]),
        "y": float(job['dec'][i]),
        "brightness": float(job['phot_g_mean_mag'][i])
    })

with open('frontend/src/realSpaceData.json', 'w') as f:
    json.dump(stars, f)

print("Saved real space data to frontend/src/realSpaceData.json!")