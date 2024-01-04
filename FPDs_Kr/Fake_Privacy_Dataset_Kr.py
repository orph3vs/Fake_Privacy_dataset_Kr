import csv
import random
from faker import Faker

def gen_carNum():  # 차량번호 생성
    if random.random() < 0.7:
        first_digits = str(random.randint(10, 99))
    else:
        first_digits = str(random.randint(100, 999))

    middle_char = random.choice(["가", "나", "다", "라", "마", "거", "너", "더", "러", "머",
                                 "버", "서", "어", "저", "고", "노", "도", "로", "모", "보",
                                 "소", "오", "조", "구", "누", "두", "루", "무", "부", "수",
                                 "우", "주", "바", "사", "아", "자", "배", "하", "허", "호",
                                 "육", "공", "해", "국", "합"])

    last_digits = str(random.randint(100, 9999)).zfill(4)

    license_plate = f"{first_digits}{middle_char}{last_digits}"

    return license_plate

def gen_passport():  # 여권번호 생성
    passport_prefix = fake.random_element(["M", "T", "S", "R", "G", "D"])
    passport_suffix = fake.random_int(1000000, 9999999)
    passport = f"{passport_prefix}{passport_suffix}"

    return passport

fake = Faker('ko-KR')

# 임의의 데이터 생성
# data = [['연번', '이름', '나이', '생년월일', '주소', '우편번호', '회사명', '직업명', '휴대전화번호', '이메일 주소', '사용자명', '카드번호', '여권번호', '차량번호']]
data = [['연번', '이름', '나이', '생년월일', '주소', '우편번호', '직업명', '휴대전화번호', '이메일 주소', '사용자명', '카드번호', '여권번호', '차량번호']]

# 주민번호 :   ssn()
for _ in range(10000):  # range 안에 생성 수 설정
    seq_num = _
    name = fake.name()
    age = fake.random_int(20, 65)  # random.randint(20, 65)
    birth = fake.date_of_birth(tzinfo=None, minimum_age=age, maximum_age=age)
    address = fake.land_address()
    zipcode = str(random.randint(0, 99999)).zfill(5)
    #   company = fake.company()    # 한글데이터 구림.
    job = fake.job()
    phoneNum = fake.numerify(text='010-####-####')  # phone_number()
    email = fake.ascii_free_email()  # email()
    #    nickName = fake.user_name()
    nickName = email.split('@')[0]  # + str(random.randint(0, 9999)).zfill(4)
    creditCard = fake.numerify(text='%###-####-####-####')  # fake.credit_card_number()
    passport = gen_passport()
    carNum = gen_carNum()
    data.append(
        [seq_num, name, age, birth, address, zipcode, job, phoneNum, email, nickName, creditCard, passport, carNum])

# CSV 파일 쓰기
file_path = 'sample_data.csv'

with open(file_path, mode='w', newline='', encoding='cp949') as file: # utf-8 로 하면 한글이 깨짐..이유를 모르겠..
    writer = csv.writer(file)
    writer.writerows(data)

print(f'CSV 파일이 생성되었습니다. 경로: {file_path}')
