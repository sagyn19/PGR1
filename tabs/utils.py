import cv2
import matplotlib.pyplot as plt

def plot_histogram(image, title):
    """Generates a Matplotlib figure for RGB histograms."""
    fig, ax = plt.subplots(figsize=(5, 3))
    colors = ('r', 'g', 'b')
    
    for i, color in enumerate(colors):
        # Calculate histogram for each channel
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        ax.plot(hist, color=color)
        ax.set_xlim([0, 256])
    
    ax.set_title(title, fontsize=10)
    ax.axis('off')  # Hide axis for cleaner look
    plt.tight_layout()
    return fig