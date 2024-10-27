import base64
import io
import re
from io import BytesIO
from typing import Optional
from uuid import uuid4
from PIL import Image
from django.core import files as django_files
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from .models import Post, PostImage


def compression_photo(
        post: Post, images: list[str | InMemoryUploadedFile]
) -> list[PostImage]:
    """Функция для сжатия качества загружаемых фото"""

    images_list: list[PostImage] = []
    for image in images:
        # Превращаем base64 в bytes
        if isinstance(image, InMemoryUploadedFile):
            byte_image = image.read()
            image.seek(0)
        else:
            byte_image = base64.b64decode(image)
        image_stream = io.BytesIO(byte_image)
        img = Image.open(image_stream)
        # Разрешение фото. При таком весит примерно 150кб
        img.thumbnail((1600, 1600))
        file = BytesIO()
        img = img.convert("RGB")
        img.save(file, format="JPEG", quality=85)
        image_content = ContentFile(file.getvalue(), name=str(uuid4()))
        file.seek(0)
        images_list.append(PostImage(post=post, image=image_content))
    return images_list
