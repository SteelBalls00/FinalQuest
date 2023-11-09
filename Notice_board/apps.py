from django.apps import AppConfig


class NoticeBoardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Notice_board'

    def ready(self):
        import Notice_board.signals