import os
import base64

def jpg_folder_to_single_txt(folder_path, output_txt="images_base64.txt"):
    """
    Encode all .jpg/.jpeg files in the folder to Base64
    and append them into a single text file. Just remove 
    "page_" and "page_hidden_" from name and copy into reader.

    Format (example line):
    'image1': 'data:image/jpeg;base64,<base64-string>,
    """
    lines = []

    for filename in os.listdir(folder_path):
        if filename.lower().endswith((".jpg", ".jpeg")):
            file_path = os.path.join(folder_path, filename)

            with open(file_path, "rb") as img_file:
                encoded = base64.b64encode(img_file.read()).decode("utf-8")

            name_no_ext = os.path.splitext(filename)[0]

            # Exactly the requested format:
            # '[file name with no extension]': 'data:image/jpeg;base64,[base64 string],
            line = f"'{name_no_ext}': 'data:image/jpeg;base64,{encoded}',"
            lines.append(line)

    output_path = os.path.join(folder_path, output_txt)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"Wrote Base64 for {len(lines)} images to {output_txt}")


if __name__ == "__main__":
    # directory where this .py file is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    jpg_folder_to_single_txt(script_dir)
