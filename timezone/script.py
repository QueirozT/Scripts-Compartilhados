import pytz
from datetime import datetime


UTC = pytz.utc
BRTZ = pytz.timezone('America/Sao_Paulo')


def converte_datetime_de_utc_para_brtz(string: str) -> datetime:
    datetime_utf = datetime.strptime(
        string, '%Y-%m-%dT%H:%M:%SZ'
        ).replace(tzinfo=UTC)

    return datetime_utf.astimezone(BRTZ)


def converte_datetime_de_brtz_para_utc(string: str) -> datetime:
    datetime_brtz = datetime.strptime(
        string, '%Y-%m-%dT%H:%M:%SZ'
        ).replace(tzinfo=BRTZ)

    return datetime_brtz.astimezone(UTC)


if __name__ == '__main__':

    exemplo = '2022-08-01T16:34:16Z'
    print(f'Data exemplo: \n{exemplo}')

    exemplo_utc = converte_datetime_de_utc_para_brtz(exemplo)
    print(f'\nConvertido de UTC para BRTZ:\n{exemplo_utc}')
    # 2022-08-01 13:34:16-03:00   

    exemplo_brtz = converte_datetime_de_brtz_para_utc(exemplo)
    print(f'\nConvertido de BRTZ para UTC:\n{exemplo_brtz}')
    # 2022-08-01 19:40:16+00:00
