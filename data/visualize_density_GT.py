import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Load the density map from the .npy file
density_map = np.load('C:\\aayush\\main\\IITK COURSE\\EE798\\researchpaper1\\final\\MPCount\\data\\sta\\train\\IMG_11_dmap.npy')

# Load the corresponding image (assuming it's in .jpg format)
image = Image.open('C:\\aayush\\main\\IITK COURSE\\EE798\\researchpaper1\\final\\MPCount\\data\\sta\\train\\IMG_11.jpg')

# Set up the figure and display both images side by side
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Display the original image
axes[0].imshow(image)
axes[0].set_title('Original Image')
axes[0].axis('off')  # Hide axes for a cleaner look

# Display the density map
im = axes[1].imshow(density_map, cmap='jet')
axes[1].set_title('GT- Density Map Visualization')
axes[1].axis('off')  # Hide axes for a cleaner look

# Add a colorbar for the density map
plt.colorbar(im, ax=axes[1], fraction=0.046, pad=0.04)

# Show the figure
plt.tight_layout()
plt.show()
