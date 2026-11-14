from astroquery.skyview import SkyView
import matplotlib.pyplot as plt
import os

print("Fetching multi-epoch/survey image cutouts from NASA SkyView...")
surveys = ["DSS1 Red", "DSS2 Red", "IRAS 100", "VGPS"]
os.makedirs("frontend/public/images", exist_ok=True)

try:
    images = SkyView.get_images(position="05h34m31.97s +22d00m52.1s", survey=surveys, pixels=400)
    for i, img in enumerate(images):
        survey_name = surveys[i] if i < len(surveys) else f"Epoch {i+1}"
        fig, ax = plt.subplots(figsize=(5, 5))
        ax.imshow(img[0].data, cmap="gray", origin="lower")
        ax.axis("off")
        filename = f"epoch_{i+1}.png"
        filepath = f"frontend/public/images/{filename}"
        plt.savefig(filepath, bbox_inches="tight", pad_inches=0, facecolor="black")
        plt.close()
        print(f"Saved {survey_name} -> {filepath}")
    print("All image cutouts successfully fetched and saved!")
except Exception as e:
    print(f"Error fetching images: {e}")

