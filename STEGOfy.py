# Import library
from steg import steg_img

def hide_message(file_path, image_path):
    s = steg_img.IMG(payload_path=file_path, image_path=image_path)
    s.hide()

def extract_message(image_path):
    s_prime = steg_img.IMG(image_path=image_path)
    s_prime.extract()

