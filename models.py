from django.db import models

DISEASES = (
    ('Tuberculosis', 'Tuberculosis'),
    ('Diphtheria', 'Diphtheria'),
    ('Tetanus', 'Tetanus'),
    ('Measles', 'Measles'),
    ('Malaria', 'Malaria'),
    ('Intestinal nematode infections', 'Intestinal nematode infections'),
    ('Dengue', 'Dengue'),
    ('Rabies', 'Rabies'),
    ('Hepatitis', 'Hepatitis'),
    ('Leprosy', 'Leprosy'),
    ('Leukemia', 'Leukemia'),
    ('Endocarditis', 'Endocarditis'),
    ('Epilepsy', 'Epilepsy'),
    ('Meningitis', 'Meningitis'),
    ('Maternal hemorrhage', 'Maternal hemorrhage '),
    )

DISEASES_DICT = dict(DISEASES)

class Input(models.Model):
    disease = models.CharField(choices=DISEASES, max_length=15)

class Diseases(models.Model):
    disease = models.CharField(choices=DISEASES, max_length=15)
