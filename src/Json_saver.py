import json

from src.abstractHh import AbstractSaver


class JsonSaver(AbstractSaver):
    def save(self, save):

        if len(save) == 0:
            print('Vacancy not found\nPlease repute')
        else:
            json.dumps(save, indent=2, ensure_ascii=False)
            return save

        # ������ ���������� �������� � ����

    pass

    def load_all(self, source: str) -> list[dict]:
        # ������ ������ ����� � ��������� ���� ��������
        pass

    def get_vacancy(self, vacancy) -> dict:
        # ������ ��������� �������� �� ����� (�������� �� �������� ��� ID)
        # ����� �������� pass, ���� �� �������������� ������������
        pass

    def delete_vacancy(self, vacancy) -> None:
        # ������ �������� �������� �� ����� (�������� �� �������� ��� ID)
        # ����� �������� pass, ���� �� �������������� ������������
        pass
