# Computer Graphics Algorithms Visualization (PGR1)

**Author:** Sagynbek Kubanychbek uulu
**Field of Study:** APIN
**Academic Year:** 2025/2026 (Winter Semester)
**Course:** Computer Graphics 1 (PGR1)

---

## 1. Project Assignment
The goal of this semester project was to create an interactive software application to demonstrate and visualize key concepts of computer graphics. The application allows the user to experiment with algorithm parameters and observe their impact on image data in real-time.

The application covers the following syllabus topics:
* **Raster Operations:** Convolution filters and edge detection.
* **Image Analysis:** Calculation and visualization of RGB histograms.
* **Geometric Transformations:** Rotation and scaling using affine matrices.
* **Image Compression:** Simulation of lossy compression (JPEG) and its effect on quality.

## 2. Solution Description
The project is designed as a local web application ("dashboard"), allowing for cross-platform execution without dependency on a specific OS (Windows/macOS/Linux).

### Architecture
The project is structured modularly. The main logic is handled by the **Streamlit** framework, which manages the GUI. The computational core uses **OpenCV** and **NumPy** libraries for matrix operations.
* `app.py`: The entry point of the application; manages navigation and layout.
* `tabs/`: A module containing the logic for individual sections (Filters, Geometry, Compression).

### Algorithms Used

#### A. Convolution Filters (Tab 1)
**Discrete 2D convolution** is implemented for image processing.
* **Principle:** A sliding window (kernel) of size $3 \times 3$ moves across the image. The new pixel value is calculated as a weighted sum of its neighbors.
* **Implementation:** Users can choose predefined kernels (Gaussian Blur, Sobel, Laplacian) or input a custom matrix.
* **Analysis:** The application calculates intensity histograms for R, G, and B channels in real-time, visualizing changes in contrast and brightness after filtering.

#### B. Geometric Transformations (Tab 2)
Transformations are realized using **Affine Matrices** ($2 \times 3$).
* For rotation and scaling, a function generates a transformation matrix combining rotation around the image center and scaling.
* A backward mapping (warp) algorithm is applied to prevent holes in the resulting image.

#### C. Compression (Tab 3)
Compression simulation uses the JPEG standard.
* The image is encoded into a memory buffer with a quality parameter (1–100). This triggers the quantization of DCT coefficients (Discrete Cosine Transform).
* The application then decodes the image back and calculates the resulting file size for comparison with the original.

---

## 3. Installation and Usage

The application is written in **Python** (version 3.8+). There are two methods to run it.

### Method A: Standard Execution (Python)
This method requires Python installed on your system.

1.  **Install Dependencies:**
    Open a terminal in the project folder and run:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run Application:**
    ```bash
    streamlit run app.py
    ```
    

### Method B: Docker Execution (Recommended for Isolation)
The project includes a `Dockerfile` for easy container build.

1.  **Build Image:**
    ```bash
    docker build -t pgr1-project .
    ```

2.  **Run Container:**
    ```bash
    docker run -p 8501:8501 pgr1-project
    ```

---

## 4. System Requirements
* **OS:** Windows, macOS, or Linux.
* **Python:** Version 3.9 or newer (if not using Docker).
* **Libraries:** Listed in `requirements.txt` (Streamlit, OpenCV, NumPy, Matplotlib).
