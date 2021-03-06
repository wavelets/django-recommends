from django.conf import settings

RECOMMENDS_STORAGE_DATABASE_ALIAS = getattr(settings, 'RECOMMENDS_STORAGE_DATABASE_ALIAS', 'recommends')
RECOMMENDS_STORAGE_COMMIT_THRESHOLD = getattr(settings, 'RECOMMENDS_STORAGE_COMMIT_THRESHOLD', 1000)
