import zipfile
import os

def extract_images(pptx_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with zipfile.ZipFile(pptx_path, 'r') as z:
        for file_info in z.infolist():
            if file_info.filename.startswith('ppt/media/'):
                original_filename = os.path.basename(file_info.filename)
                target_path = os.path.join(output_dir, original_filename)
                with open(target_path, 'wb') as f:
                    f.write(z.read(file_info.filename))
                print(f"Extracted: {target_path}")

if __name__ == "__main__":
    pptx_file = "d:/medical_report_generation/presentation_deep_learning.pptx"
    output_folder = "d:/medical_report_generation/images/"
    extract_images(pptx_file, output_folder)
