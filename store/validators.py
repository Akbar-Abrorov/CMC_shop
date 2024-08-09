from rest_framework.exceptions import ValidationError


def validate_file_size(file):
    max_size_kb = 500

    if file.size > max_size_kb * 1024:
        raise ValidationError(f'File size must be less than or equal to {max_size_kb} KB!.')